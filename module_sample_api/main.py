import logging
import sys
import os
import uvicorn
from fastapi import FastAPI, APIRouter
import importlib
from pkgutil import iter_modules
from fastapi.middleware.cors import CORSMiddleware
from argparse import ArgumentParser
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module_sample_api.configurations.app_conf import AppConf
from module_sample_api.configurations.swagger_conf import SwaggerConf
from module_sample_api.middlewares.limit_upload_size_middleware import LimitUploadSizeMiddleware
from module_sample_api.configurations.logging_config import setup_logging
from module_sample_api.middlewares.logging_middleware import LoggingMiddleware

# [FastAPI 실행 Main]
# FastAPI 객체 생성
app = FastAPI(
    # swagger Docs 접속 가능 설정
    docs_url="/docs" if AppConf.swagger_docs_enable else None,
    redoc_url="/redoc" if AppConf.swagger_docs_enable else None,
    openapi_url="/openapi.json" if AppConf.swagger_docs_enable else None
)
AppConf.app = app

# python 실행 명령어에서 profile 인자 받기 (소문자로 인식, 실행 예시 : python main.py --profile dev)
parser = ArgumentParser(description="Run FastAPI application")
parser.add_argument('--profile', type=str, default=AppConf.server_profile,
                    help="Specify the profile (default: 'local')")
args = parser.parse_args()
AppConf.server_profile = args.profile.lower()

# 로깅 설정 적용
setup_logging()

# Swagger 설정 적용
AppConf.app.openapi = lambda: SwaggerConf.custom_openapi(AppConf.app)

# 현재 파일이 속한 디렉토리 경로
AppConf.module_folder_path = os.path.dirname(os.path.abspath(__file__))
# 디렉토리 경로에서 폴더명만 추출 (main.py 파일은 모듈 폴더 바로 안에 위치 해야 함)
folder_name = os.path.basename(AppConf.module_folder_path)
# controllers 디렉토리에 있는 모든 라우터 등록
controllers_package_name = "controllers"
for _, module_name, _ in iter_modules([AppConf.module_folder_path + "/" + controllers_package_name]):
    module = importlib.import_module(f"{folder_name}.{controllers_package_name}.{module_name}")
    if hasattr(module, "router") and isinstance(module.router, APIRouter):
        AppConf.app.include_router(module.router)

# Jinja2Templates HTML 템플릿 위치 설정
AppConf.jinja2Templates = Jinja2Templates(directory=f"{folder_name}/z_resources/templates")

# static 위치 설정
AppConf.app.mount(
    # 클라이언트가 접근할 경로입니다. 예: http://localhost:8000/static/for_global/font.css
    "/static",
    # 실제 서버 파일 시스템 상의 디렉토리입니다. 이 경로의 파일을 클라이언트에게 서빙합니다.
    StaticFiles(directory=f"{folder_name}/z_resources/static"),
    # 템플릿에서 url_for("static", path="...") 호출 시 사용할 이름입니다.
    name="static"
)

# 파일 업로드 사이즈 제한 미들웨어 등록
AppConf.app.add_middleware(LimitUploadSizeMiddleware)
AppConf.app.add_middleware(
    CORSMiddleware,
    allow_origins=AppConf.cors_allow_origins,  # 모든 origin 허용 (또는 ["https://example.com"] 등 명시적으로 설정)
    allow_credentials=AppConf.cors_allow_credentials,
    allow_methods=AppConf.cors_allow_methods,  # GET, POST, PUT, DELETE 등
    allow_headers=AppConf.cors_allow_headers
)
AppConf.app.add_middleware(LoggingMiddleware)

# FastAPI 서버 실행
# main.py 위쪽 코드 부터 순차 실행 후 __main__ 코드 실행. 그리고 다시 위 코드가 __main__ 앞까지 실행 됩니다.
if __name__ == "__main__":
    # 서버 실행 정보 로깅
    logging.info("<<FastAPI Startup>>")
    logging.info(f"port : {AppConf.uvicorn_port}")
    logging.info(f"serverName : {AppConf.server_name}")
    logging.info(f"Profile : {AppConf.server_profile}")
    logging.info(f"serverUuid : {AppConf.server_uuid}")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=AppConf.uvicorn_port,
        reload=False  # 개발 환경에서 코드 변경시 자동으로 서버 재시작 기능(오동작 우려가 있기에 False 고정)
    )
