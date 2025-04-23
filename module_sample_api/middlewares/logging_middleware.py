import logging
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from datetime import datetime
import json
import time
from typing import Callable

# [요청/응답 자동 로깅]
logger = logging.getLogger("request_logger")

VISIBLE_CONTENT_TYPES = [
    "application/json",
    "application/xml",
    "text/plain",
    "text/html",
    "application/*+json",
    "application/*+xml",
]


def is_visible_content_type(content_type: str | None) -> bool:
    if content_type:
        for visible_type in VISIBLE_CONTENT_TYPES:
            if content_type.startswith(visible_type.replace("*", "")):
                return True
    return False


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request_time = datetime.utcnow()
        client_ip = request.client.host
        method = request.method
        url = str(request.url)

        request_body = await request.body()
        headers = dict(request.headers)

        try:
            # 응답 얻기 (response body를 복사할 수 있도록 stream을 사용)
            start_time = time.time()
            response = await call_next(request)
            process_time = int((time.time() - start_time) * 1000)

            # Response body 복사
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk

            # 새 Response 객체로 다시 wrapping
            new_response = Response(
                content=response_body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type
            )

            req_body_str = request_body.decode("utf-8", errors="ignore") if is_visible_content_type(
                headers.get("content-type")) else f"{len(request_body)} bytes content"
            res_body_str = response_body.decode("utf-8", errors="ignore") if is_visible_content_type(
                response.headers.get("content-type")) else f"{len(response_body)} bytes content"

            log_json = {
                "request_info": {
                    "request_time": str(request_time),
                    "end_point": f"{method} {url}",
                    "client_ip": client_ip,
                    "request_headers": headers,
                    "request_body": req_body_str,
                },
                "response_info": {
                    "response_status": f"{response.status_code}",
                    "processing_duration_ms": process_time,
                    "response_headers": dict(response.headers),
                    "response_body": res_body_str,
                },
            }

            if 500 <= response.status_code:
                logger.error(">>ApiFilterLog>>\n%s", json.dumps(log_json, indent=4))
            else:
                logger.info(">>ApiFilterLog>>\n%s", json.dumps(log_json, indent=4))

            return new_response

        except Exception as e:
            logger.exception("Unhandled error during request logging: %s", e)
            raise e
