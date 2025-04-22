import uuid
import time


# [API 설정 상수]
class AppConf:
    # 서버 고유값 (런타임 시에 고정되도록 생성)
    server_uuid = f"{int(time.time() * 1000)}/{uuid.uuid4()}"

    # 서버 실행 프로필(local, dev, profile, ...)
    server_profile = "local"

    # controllers 폴더 위치(main.py 기중)
    controllers_package_name = "controllers"

    # 서버가 어떤 IP 주소에서 접근을 허용할지를 설정하는 옵션
    # "127.0.0.1" 또는 "localhost"	로컬 컴퓨터에서만 접근 가능 (외부에서 접근 불가)
    # "0.0.0.0"	모든 IP에서 접근 허용 (같은 네트워크의 다른 장치나 외부에서도 접속 가능)
    unicorn_host = "0.0.0.0"

    # 서버 점유 포트
    unicorn_port = 8080

    # 코드를 수정 하면 서버를 자동으로 재시작(reload) 해주는 개발용 기능
    unicorn_reload = True

    # 파일 업로드 제한 사이즈
    max_upload_size = 10 * 1024 * 1024  # 10MB

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
