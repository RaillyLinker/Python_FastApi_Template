from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


# [Swagger 문서 설정]
class SwaggerConf:
    @staticmethod
    def custom_openapi(app: FastAPI):
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = (
            get_openapi(
                title="SAMPLE-API",
                description="API 명세입니다.",
                version="1.0.0",
                contact={
                    "name": "Railly Linker",
                    "url": "https://railly-linker.tistory.com",
                    "email": "raillylinker@gmail.com",
                },
                license_info={
                    "name": "MIT",
                    "url": "https://opensource.org/licenses/MIT",
                },
                routes=app.routes
            )
        )

        # 모든 경로에 400, 500 응답을 추가
        for path in openapi_schema["paths"].values():
            for method in path.values():
                responses = method.setdefault("responses", {})
                responses.setdefault("400", {"description": "잘못된 요청입니다."})
                responses.setdefault("500", {"description": "서버 내부 오류입니다."})

        app.openapi_schema = openapi_schema
        return app.openapi_schema
