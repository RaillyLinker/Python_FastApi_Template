from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from typing import Callable, Awaitable
import module_sample_api.configurations.app_conf as app_conf


# [파일 업로드 사이즈 제한 미들웨어]
# 클라이언트 측은 전송하는 데이터 스트림을 전부 비운 후 응답을 받기에 응답이 느릴 수도 있음.
# 고로 이 미들웨어는 서버측 보호를 위한 안전장치이고, 실제 파일 업로드 컷은 클라이언트 측 로직에서 처리하도록 할 것.
class LimitUploadSizeMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self,
            request: Request,
            call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        content_length = request.headers.get("Content-Length")
        if content_length and int(content_length) > app_conf.max_upload_size:
            max_size_mb = app_conf.max_upload_size / (1024 * 1024)
            return JSONResponse(
                status_code=413,
                content={
                    "detail": f"File too large. You cannot upload files larger than {max_size_mb:.2f} MB."
                }
            )
        return await call_next(request)
