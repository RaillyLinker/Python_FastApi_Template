from uuid import uuid4
from time import time
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI


# [API 설정 상수]
class AppConf:
    # ---- (자동 할당 상수) ----
    # 서버 실행 프로필(local, dev, profile, ...)
    # 서버 실행시 python 입력값을 기반으로 입력됨
    # python 입력값이 없을시 아래 설정값이 기본
    # 이 프로필을 기반으로 아래 값들을 설정 해도 됩니다.
    server_profile = "local"

    # FastApi app
    app: FastAPI

    # 서버 고유값 (런타임 시에 고정되도록 생성)
    server_uuid = f"{int(time() * 1000)}/{uuid4()}"

    # main.py 파일의 부모 폴더 경로
    # ex : C:\dev\python\Python_Fastapi_Template\module_sample_api
    module_folder_path = ""

    # jinja2 HTML Templates 객체
    jinja2Templates: Jinja2Templates

    # ---- (수동 설정 상수) ----
    # 서버명(로그 파일 등을 이 기준으로 사용하기에 모듈별 수정 필요)
    server_name = "template"

    # 서버 점유 포트
    uvicorn_port = 8080

    # 파일 업로드 제한 사이즈
    max_upload_size = 10 * 1024 * 1024  # 10MB

    # 스웨거 문서 오픈 여부
    swagger_docs_enable = True

    # CORS Origins
    # 허용 origin 전체 ["*"], 또는 특정 ["https://example.com"]
    cors_allow_origins = ["*"]

    # CORS Credentials
    # 쿠키, 인증 정보(Authorization 헤더 등)를 포함한 요청을 허용할지 여부
    cors_allow_credentials = True

    # CORS Methods
    # 허용 Method GET, POST, PUT, DELETE 등
    cors_allow_methods = ["*"]

    # CORS Headers
    # 요청 시 어떤 헤더들을 허용할지 설정
    cors_allow_headers = ["*"]

    # Swagger 문서 공지
    swagger_doc_title = "TEMPLATE"
    swagger_doc_description = "API 명세입니다."
    swagger_doc_version = "1.0.0"
    swagger_doc_contact = {
        "name": "Railly Linker",
        "url": "https://railly-linker.tistory.com",
        "email": "raillylinker@gmail.com",
    }
    swagger_doc_license_info = {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
