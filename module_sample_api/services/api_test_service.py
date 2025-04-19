# main.py
from fastapi import FastAPI
from controllers import user_controller

app = FastAPI()

# 라우터 등록
app.include_router(user_controller.router)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}
