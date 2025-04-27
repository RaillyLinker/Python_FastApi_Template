from collections.abc import Sequence
from functools import wraps
from typing import Any, Callable
import module_sample_sql_alchemy.utils.sql_alchemy_util as sql_alchemy_util
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import db_timezone


# (SQLAlchemy 레포지토리 함수 위에 붙이는 데코레이터)
def sql_alchemy_func(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if result is None:
            return result

        if isinstance(result, Sequence) and not isinstance(result, (str, bytes)):
            sql_alchemy_util.apply_timezone_to_datetime_fields_in_list(result, db_timezone)
        else:
            sql_alchemy_util.apply_timezone_to_datetime_fields(result, db_timezone)

        return result

    return wrapper
