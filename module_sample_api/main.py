import sys
import os
import uvicorn
import fastapi
import importlib
import pkgutil
import fastapi.middleware.cors as cors_middle_ware
import argparse  # argparse 라이브러리 추가

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import module_sample_api.configurations.app_conf as app_conf
import module_sample_api.configurations.swagger_conf as swagger_conf
import module_sample_api.middlewares.limit_upload_size_middleware as limit_upload_size_middleware

# [FastAPI 실행 Main]
# python 실행 명령어에서 profile 인자 받기 (소문자로 인식, 실행 예시 : python main.py --profile dev)
parser = argparse.ArgumentParser(description="Run FastAPI application")
parser.add_argument('--profile', type=str, default='local', help="Specify the profile (default: 'local')")
args = parser.parse_args()
app_conf.AppConf.server_profile = args.profile.lower()

# 현재 파일이 속한 디렉토리 경로
dir_path = os.path.dirname(os.path.abspath(__file__))

# 디렉토리 경로에서 폴더명만 추출 (main.py 파일은 모듈 폴더 바로 안에 위치 해야 함)
folder_name = os.path.basename(dir_path)

# FastAPI 객체 생성
app = fastapi.FastAPI()

# Swagger 설정 적용
app.openapi = lambda: swagger_conf.SwaggerConf.custom_openapi(app)

# controllers 디렉토리에 있는 모든 라우터 등록
for _, module_name, _ in pkgutil.iter_modules([dir_path + "/" + app_conf.AppConf.controllers_package_name]):
    module = importlib.import_module(f"{folder_name}.{app_conf.AppConf.controllers_package_name}.{module_name}")
    if hasattr(module, "router") and isinstance(module.router, fastapi.APIRouter):
        app.include_router(module.router)

# 파일 업로드 사이즈 제한 미들웨어 등록
app.add_middleware(limit_upload_size_middleware.LimitUploadSizeMiddleware)
app.add_middleware(
    cors_middle_ware.CORSMiddleware,
    allow_origins=app_conf.AppConf.cors_allow_origins,  # 모든 origin 허용 (또는 ["https://example.com"] 등 명시적으로 설정)
    allow_credentials=app_conf.AppConf.cors_allow_credentials,
    allow_methods=app_conf.AppConf.cors_allow_methods,  # GET, POST, PUT, DELETE 등
    allow_headers=app_conf.AppConf.cors_allow_headers
)

# FastAPI 서버 실행
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_conf.AppConf.unicorn_host,
        port=app_conf.AppConf.unicorn_port,
        reload=app_conf.AppConf.unicorn_reload
    )
