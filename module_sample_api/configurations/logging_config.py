import logging
from logging.handlers import TimedRotatingFileHandler
import os
import pytz
from datetime import datetime
import module_sample_api.configurations.app_conf as app_conf


def custom_time():
    seoul_tz = pytz.timezone("Asia/Seoul")
    return datetime.now(seoul_tz).timetuple()


class CustomFormatter(logging.Formatter):
    converter = custom_time

    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=pytz.timezone("Asia/Seoul"))
        millis = int(dt.microsecond / 1000)  # 마이크로초를 밀리초로 변환
        s = dt.strftime("%Y_%m_%d_T_%H_%M_%S") + f"_{millis:03d}_{dt.tzname()}"
        return s


# [logging 라이브러리 설정]
def setup_logging():
    log_dir = f"./by_product_files/{app_conf.AppConf.server_name}/logs/{app_conf.AppConf.server_profile}"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"{app_conf.AppConf.server_profile}_current_log.log")

    formatter = CustomFormatter(
        '[ls] [%(asctime)s] [%(levelname)-5s] [%(message)s] [le]',
        datefmt='%Y_%m_%dT%H_%M_%S_%f %Z'
    )

    file_handler = TimedRotatingFileHandler(
        log_file, when="midnight", interval=1, backupCount=30, encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 루트 로거
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers.clear()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # uvicorn 관련 로거들도 직접 설정
    for logger_name in ["uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.handlers.clear()
        logger.propagate = True  # 루트 로거로 전달되도록 허용
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
