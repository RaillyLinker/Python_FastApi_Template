from sqlalchemy import select, DateTime, and_, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect
import tzlocal
from typing import List, Sequence, Optional
from module_sample_sql_alchemy.decorators.sql_alchemy_deco import sql_alchemy_func
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import db_timezone
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_fk_test_many_to_one_child import \
    Db1TemplateFkTestManyToOneChild
import \
    module_sample_sql_alchemy.sql_alchemy_objects.db1_main.value_objects.template_fk_test_many_to_one_child_vo as value_objects


# [SqlAlchemy 레포지토리]
# 모든 함수에는 @sql_alchemy_func 를 붙이고, 이로 인하여 반환값은 단일 값을 반환하거나,
# return entities, total_elements 이렇게 return 값이 많을 경우 최대 2개만을 허용합니다.

# 데이터 save(동일 pk 가 존재 하면 update, 없다면 insert)
@sql_alchemy_func
async def save(db: AsyncSession, entity: Db1TemplateFkTestManyToOneChild) -> Db1TemplateFkTestManyToOneChild:
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
    stmt = select(Db1TemplateFkTestManyToOneChild)
    result = await db.execute(stmt)
    entity_list = result.scalars().all()

    for entity in entity_list:
        await db.delete(entity)


# 데이터 pk 로 delete
@sql_alchemy_func
async def delete_by_id(db: AsyncSession, pk: int):
    stmt = select(Db1TemplateFkTestManyToOneChild).where(Db1TemplateFkTestManyToOneChild.uid == pk)
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    if entity:
        await db.delete(entity)


# 모든 데이터 검색
@sql_alchemy_func
async def find_all(db: AsyncSession) -> Sequence[Db1TemplateFkTestManyToOneChild]:
    stmt = select(Db1TemplateFkTestManyToOneChild)
    result = await db.execute(stmt)
    entity_list = result.scalars().all()
    return entity_list


# 데이터 pk 로 검색(0 or 1 result)
@sql_alchemy_func
async def find_by_id(db: AsyncSession, pk: int) -> Optional[Db1TemplateFkTestManyToOneChild]:
    stmt = select(Db1TemplateFkTestManyToOneChild).where(Db1TemplateFkTestManyToOneChild.uid == pk)
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    return entity


# ---- (커스텀 쿼리 함수 추가 공간) ----
@sql_alchemy_func
async def find_all_by_fk_test_parent_uid_and_row_delete_date_str(
        db: AsyncSession,
        fk_test_parent_uid: int,
        row_delete_date_str: str
) -> Sequence[Db1TemplateFkTestManyToOneChild]:
    stmt = select(Db1TemplateFkTestManyToOneChild).where(
        and_(
            Db1TemplateFkTestManyToOneChild.fk_test_parent_uid == fk_test_parent_uid,
            Db1TemplateFkTestManyToOneChild.row_delete_date_str == row_delete_date_str
        )
    )
    result = await db.execute(stmt)
    entity_list = result.scalars().all()
    return entity_list


@sql_alchemy_func
async def find_all_from_template_fk_test_many_to_one_child_inner_join_parent_by_not_deleted(
        db: AsyncSession
) -> List[value_objects.FindAllFromTemplateFkTestManyToOneChildInnerJoinParentByNotDeletedOutputVo]:
    query = text("""
            SELECT 
            fk_test_many_to_one_child.uid AS childUid, 
            fk_test_many_to_one_child.child_name AS childName, 
            fk_test_many_to_one_child.row_create_date AS childCreateDate, 
            fk_test_many_to_one_child.row_update_date AS childUpdateDate, 
            fk_test_parent.uid AS parentUid, 
            fk_test_parent.parent_name AS parentName 
            FROM 
            template.fk_test_many_to_one_child AS fk_test_many_to_one_child 
            INNER JOIN 
            template.fk_test_parent AS fk_test_parent 
            ON 
            fk_test_parent.uid = fk_test_many_to_one_child.fk_test_parent_uid AND 
            fk_test_parent.row_delete_date_str = '/' 
            WHERE 
            fk_test_many_to_one_child.row_delete_date_str = '/' 
    """)

    result = await db.execute(query, {})
    rows = result.mappings().all()  # key-value dict로 가져옴

    output = [
        value_objects.FindAllFromTemplateFkTestManyToOneChildInnerJoinParentByNotDeletedOutputVo(
            child_uid=row["childUid"],
            child_name=row["childName"],
            child_create_date=row["childCreateDate"],
            child_update_date=row["childUpdateDate"],
            parent_uid=row["parentUid"],
            parent_name=row["parentName"]
        )
        for row in rows
    ]

    return output
