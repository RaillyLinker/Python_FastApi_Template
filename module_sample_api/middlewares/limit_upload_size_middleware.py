from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import module_sample_api.configurations.app_conf as app_conf


# [파일 업로드 사이즈 제한 미들웨어]
# 클라이언트 측은 전송하는 데이터 스트림을 전부 비운 후 응답을 받기에 응답이 느릴 수도 있음.
# 고로 이 미들웨어는 서버측 보호를 위한 안전장치이고, 실제 파일 업로드 컷은 클라이언트 측 로직에서 처리하도록 할 것.
class LimitUploadSizeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("Content-Length")
        if content_length and int(content_length) > app_conf.AppConf.max_upload_size:
            return Response("파일이 너무 큽니다.", status_code=413)  # Payload Too Large
        return await call_next(request)
