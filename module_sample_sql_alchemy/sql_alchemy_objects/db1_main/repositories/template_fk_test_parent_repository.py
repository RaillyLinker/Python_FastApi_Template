from sqlalchemy import select, DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect
import tzlocal
from typing import Sequence, Optional
from module_sample_sql_alchemy.decorators.sql_alchemy_deco import sql_alchemy_func
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import db_timezone
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_fk_test_parent import \
    Db1TemplateFkTestParent
import \
    module_sample_sql_alchemy.sql_alchemy_objects.db1_main.value_objects.template_fk_test_parent_vo as template_fk_test_parent_vo


# [SqlAlchemy 레포지토리]
# 모든 함수에는 @sql_alchemy_func 를 붙이고, 이로 인하여 반환값은 단일 값을 반환하거나,
# return entities, total_elements 이렇게 return 값이 많을 경우 최대 2개만을 허용합니다.

# 데이터 save(동일 pk 가 존재 하면 update, 없다면 insert)
@sql_alchemy_func
async def save(db: AsyncSession, entity: Db1TemplateFkTestParent) -> Db1TemplateFkTestParent:
    # datetime 필드 자동 탐지 및 타임존 변환
    mapper = inspect(entity.__class__)
    for column in mapper.columns:
        # print(f"Inspecting column: {column.name}({column.type})")  # 디버깅용: 어떤 컬럼을 확인 중인지 출력
        if isinstance(column.type, DateTime):  # Datetime 타입 변수만 탐지
            attr_name = column.name  # 컬럼명 ex : row_create_date
            value = getattr(entity, attr_name)  # 입력된 값 ex : 2025-04-26 10:14:13.335610
            # print(f">>>> attr_name : {attr_name}, value : {value}")

            if value is not None:
                if value.tzinfo is None:  # 타임존 설정 안한 경우
                    local_tz = tzlocal.get_localzone()  # 로컬 타임존 예: Asia/Seoul
                    value = value.replace(tzinfo=local_tz)

                # DB 타임존 설정으로 타임존 변경
                value = value.astimezone(db_timezone)

                # 객체 내 변수 값 수정
                setattr(entity, attr_name, value)

    db.add(entity)
    await db.flush()
    await db.refresh(entity)

    return entity


# 모든 데이터 삭제
@sql_alchemy_func
async def delete_all(db: AsyncSession):
    stmt = select(Db1TemplateFkTestParent)
    result = await db.execute(stmt)
    entity_list = result.scalars().all()

    for entity in entity_list:
        await db.delete(entity)


# 데이터 pk 로 delete
@sql_alchemy_func
async def delete_by_id(db: AsyncSession, pk: int):
    stmt = select(Db1TemplateFkTestParent).where(Db1TemplateFkTestParent.uid == pk)
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    if entity:
        await db.delete(entity)


# 모든 데이터 검색
@sql_alchemy_func
async def find_all(db: AsyncSession) -> Sequence[Db1TemplateFkTestParent]:
    stmt = select(Db1TemplateFkTestParent)
    result = await db.execute(stmt)
    entity_list = result.scalars().all()
    return entity_list


# 데이터 pk 로 검색(0 or 1 result)
@sql_alchemy_func
async def find_by_id(db: AsyncSession, pk: int) -> Optional[Db1TemplateFkTestParent]:
    stmt = select(Db1TemplateFkTestParent).where(Db1TemplateFkTestParent.uid == pk)
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    return entity

# ---- (커스텀 쿼리 함수 추가 공간) ----
