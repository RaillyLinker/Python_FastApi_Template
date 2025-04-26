from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import module_sample_api.configurations.app_conf as app_conf


# [Swagger 문서 설정]
class SwaggerConf:
    @staticmethod
    def custom_openapi(app: FastAPI):
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = (
            get_openapi(
                title=app_conf.swagger_doc_title,
                description=app_conf.swagger_doc_description,
                version=app_conf.swagger_doc_version,
                contact=app_conf.swagger_doc_contact,
                license_info=app_conf.swagger_doc_license_info,
                routes=app.routes
            )
        )

        # 모든 경로에 400, 500 응답을 추가
        for path in openapi_schema["paths"].values():
            for method in path.values():
                responses = method.setdefault("responses", {})
                responses.setdefault("400", {"description": "Bad Request"})
                responses.setdefault("500", {"description": "Internal Server Error"})

        app.openapi_schema = openapi_schema
        return app.openapi_schema
