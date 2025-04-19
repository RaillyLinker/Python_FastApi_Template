import importlib
import pkgutil
from fastapi import FastAPI, APIRouter
import uvicorn

# [FastAPI 실행 Main]
# FastAPI 객체 생성
app = FastAPI()

# Controllers 경로 지정
package_name = "controllers"

# controllers 디렉토리에 있는 모든 라우터 등록
for _, module_name, _ in pkgutil.iter_modules([package_name]):
    module = importlib.import_module(f"{package_name}.{module_name}")
    if hasattr(module, "router") and isinstance(module.router, APIRouter):
        app.include_router(module.router)

# FastAPI 서버 실행 (포트 8080으로 설정)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
