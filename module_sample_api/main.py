import uvicorn
import fastapi
import importlib
import pkgutil
import os
import module_sample_api.configurations.app_conf as app_conf
import module_sample_api.configurations.swagger_conf as swagger_conf

# [FastAPI 실행 Main]
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

# FastAPI 서버 실행
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_conf.AppConf.unicorn_host,
        port=app_conf.AppConf.unicorn_port,
        reload=app_conf.AppConf.unicorn_reload
    )
