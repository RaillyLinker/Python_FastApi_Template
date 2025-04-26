from sqlalchemy.inspection import inspect
from sqlalchemy.types import DateTime
from typing import Sequence


# (Entity 안의 모든 datetime 에 타임존 정보 입력)
def apply_timezone_to_datetime_fields(entity, timezone):
    if entity is None:
        return

    mapper = inspect(entity.__class__)
    for column in mapper.columns:
        if isinstance(column.type, DateTime):
            attr_name = column.name
            value = getattr(entity, attr_name)

            if value is not None:
                value = value.replace(tzinfo=timezone)
                setattr(entity, attr_name, value)


# (Entity 리스트 안의 모든 datetime 에 타임존 정보 입력)
def apply_timezone_to_datetime_fields_in_list(entities: Sequence, timezone):
    if not entities:
        return

    for entity in entities:
        apply_timezone_to_datetime_fields(entity, timezone)
