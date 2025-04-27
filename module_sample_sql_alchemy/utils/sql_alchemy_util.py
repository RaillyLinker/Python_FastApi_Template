from sqlalchemy.inspection import inspect
from sqlalchemy.types import DateTime
from typing import Sequence
from pydantic import BaseModel
from datetime import datetime


# (Entity 안의 모든 datetime 에 타임존 정보 입력)
def apply_timezone_to_datetime_fields(entity, db_timezone):
    if entity is None:
        return

    # SQLAlchemy 엔티티인지 확인
    if hasattr(entity, '__mapper__'):
        # SQLAlchemy Entity 처리
        mapper = inspect(entity.__class__)
        for column in mapper.columns:
            if isinstance(column.type, DateTime):
                attr_name = column.name
                value = getattr(entity, attr_name)

                if value is not None:
                    value = value.replace(tzinfo=db_timezone)
                    setattr(entity, attr_name, value)

    # Pydantic 모델인지 확인
    elif isinstance(entity, BaseModel):
        # Pydantic 모델 처리
        for attr_name, value in entity.model_dump().items():
            if isinstance(value, datetime):
                if value.tzinfo is None:
                    new_value = value.replace(tzinfo=db_timezone)
                    setattr(entity, attr_name, new_value)


# (Entity 리스트 안의 모든 datetime 에 타임존 정보 입력)
def apply_timezone_to_datetime_fields_in_list(entities: Sequence, db_timezone):
    if not entities:
        return

    for entity in entities:
        apply_timezone_to_datetime_fields(entity, db_timezone)
