from collections.abc import Sequence
from functools import wraps
from typing import Any, Callable, Tuple
import module_sample_sql_alchemy.utils.sql_alchemy_util as sql_alchemy_util
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import db_timezone
from sqlalchemy.ext.declarative import DeclarativeMeta


# (SQLAlchemy 레포지토리 함수 위에 붙이는 데코레이터)
def sql_alchemy_func(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if result is None:
            return result

        # SQLAlchemy 모델인지를 확인하는 함수
        def is_sqlalchemy_model(obj):
            return isinstance(obj, object) and hasattr(obj, '__class__') and isinstance(obj.__class__, DeclarativeMeta)

        # 튜플일 경우
        if isinstance(result, Tuple):
            # 첫 번째 요소가 Sequence인 경우 apply_timezone_to_datetime_fields_in_list
            if isinstance(result[0], Sequence) and not isinstance(result[0], (str, bytes, int)):
                sql_alchemy_util.apply_timezone_to_datetime_fields_in_list(result[0], db_timezone)
            elif is_sqlalchemy_model(result[0]):  # Entity 객체인 경우
                sql_alchemy_util.apply_timezone_to_datetime_fields(result[0], db_timezone)

            # 두 번째 요소가 Sequence인 경우 apply_timezone_to_datetime_fields_in_list
            if isinstance(result[1], Sequence) and not isinstance(result[1], (str, bytes, int)):
                sql_alchemy_util.apply_timezone_to_datetime_fields_in_list(result[1], db_timezone)
            elif is_sqlalchemy_model(result[1]):  # Entity 객체인 경우
                sql_alchemy_util.apply_timezone_to_datetime_fields(result[1], db_timezone)

        # 일반적인 경우 (리스트나 단일 객체)
        elif isinstance(result, Sequence) and not isinstance(result, (str, bytes, int)):
            sql_alchemy_util.apply_timezone_to_datetime_fields_in_list(result, db_timezone)
        elif is_sqlalchemy_model(result):  # Entity 객체인 경우
            sql_alchemy_util.apply_timezone_to_datetime_fields(result, db_timezone)

        return result

    return wrapper
