import uuid
import time


class AppConf:
    # 서버 고유값 (런타임 시에 고정되도록 생성)
    server_uuid = f"{int(time.time() * 1000)}/{uuid.uuid4()}"

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
