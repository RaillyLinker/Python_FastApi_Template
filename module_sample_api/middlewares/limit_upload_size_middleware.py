from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import module_sample_api.configurations.app_conf as app_conf


# [파일 업로드 사이즈 제한 미들웨어]
class LimitUploadSizeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("Content-Length")
        if content_length and int(content_length) > app_conf.AppConf.max_upload_size:
            return Response("파일이 너무 큽니다.", status_code=413)  # Payload Too Large
        return await call_next(request)
