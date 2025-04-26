from sqlalchemy import select
from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect
import tzlocal
import module_sample_sql_alchemy.utils.sql_alchemy_util as sql_alchemy_util
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_test_data import Db1TemplateTestData
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import db_timezone


# [SqlAlchemy 레포지토리]
# 데이터 변경 함수 사용시 commit, rollback 처리를 해주세요.

# 데이터 save(동일 pk 가 존재 하면 update, 없다면 insert)
async def save(db: AsyncSession, entity: Db1TemplateTestData):
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

    # Entity 안의 datetime 에 타임존 정보 입력
    sql_alchemy_util.apply_timezone_to_datetime_fields(entity, db_timezone)

    return entity


# 모든 데이터 삭제
async def delete_all(db: AsyncSession):
    stmt = select(Db1TemplateTestData)
    result = await db.execute(stmt)
    entity_list = result.scalars().all()

    for entity in entity_list:
        await db.delete(entity)


# 데이터 pk 로 delete
async def delete_by_id(db: AsyncSession, pk: int):
    stmt = select(Db1TemplateTestData).where(Db1TemplateTestData.uid == pk)
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    if entity:
        await db.delete(entity)


# 모든 데이터 검색
async def find_all(db: AsyncSession):
    stmt = select(Db1TemplateTestData)
    result = await db.execute(stmt)
    entity_list = result.scalars().all()
    # Entity 안의 datetime 에 타임존 정보 입력
    sql_alchemy_util.apply_timezone_to_datetime_fields_in_list(entity_list, db_timezone)
    return entity_list


# 데이터 pk 로 검색(0 or 1 result)
async def find_by_id(db: AsyncSession, pk: int):
    stmt = select(Db1TemplateTestData).where(Db1TemplateTestData.uid == pk)
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    # Entity 안의 datetime 에 타임존 정보 입력
    sql_alchemy_util.apply_timezone_to_datetime_fields(entity, db_timezone)
    return entity
