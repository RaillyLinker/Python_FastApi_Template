import logging
import os
import tzlocal
import datetime
import concurrent_log_handler
import module_sample_sql_alchemy.configurations.app_conf as app_conf


# [로깅 포메터]
class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.datetime.fromtimestamp(record.created, tz=tzlocal.get_localzone())
        millis = int(dt.microsecond / 1000)  # 마이크로초를 밀리초로 변환
        s = dt.strftime("%Y_%m_%d_T_%H_%M_%S") + f"_{millis:03d}_{dt.tzname()}"
        return s


# [logging 라이브러리 설정]
def setup_logging():
    # 메시지 포멧 설정
    message_format = '[ls] [%(asctime)s] [%(levelname)-5s] [%(message)s] [le]'

    # 로깅 레벨 설정
    log_level = logging.INFO

    # 로그 저장 위치 설정 및 생성(프로젝트 루트의 by_product_files 안의 모듈명 안에 logs 로 저장)
    log_dir = f"./by_product_files/{app_conf.AppConf.server_name}/logs/{app_conf.AppConf.server_profile}"
    os.makedirs(log_dir, exist_ok=True)

    # 로깅 포메터 생성
    formatter = CustomFormatter(message_format)

    log_file = os.path.join(log_dir, f"{app_conf.AppConf.server_profile}_logfile.log")

    # 로그 파일 생성 핸들러
    # 파일 크기가 설정 크기를 넘어서면 로그 파일 분할(오래된 파일일수록 뒤에 붙은 숫자가 커짐)
    file_handler = concurrent_log_handler.ConcurrentRotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 파일 크기 10MB
        backupCount=30,  # 파일 최대 보관 개수
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 루트 로거
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.handlers.clear()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # uvicorn 관련 로거들도 직접 설정
    for logger_name in ["uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        logger.handlers.clear()
        logger.propagate = False  # 루트로 전파 방지
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
