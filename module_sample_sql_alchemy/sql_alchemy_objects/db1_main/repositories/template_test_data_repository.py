from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_test_data import Db1TemplateTestData
import module_sample_sql_alchemy.sql_alchemy_objects.db1_main.value_objects as value_objects
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


# [SqlAlchemy 레포지토리]
# 데이터 변경 함수 사용시 commit, rollback 처리를 해주세요.

# 데이터 save(동일 pk 가 존재 하면 update, 없다면 insert)
async def save(db: AsyncSession, entity: Db1TemplateTestData):
    db.add(entity)
    await db.flush()
    return entity


# 데이터 pk 로 delete
async def delete_by_id(db: AsyncSession, pk: int):
    stmt = select(Db1TemplateTestData).where(Db1TemplateTestData.uid == pk)
    result = await db.execute(stmt)
    obj = result.scalar_one_or_none()
    if obj:
        await db.delete(obj)


# 데이터 pk 로 검색(0 or 1 result)
async def find_by_id(db: AsyncSession, pk: int):
    stmt = select(Db1TemplateTestData).where(Db1TemplateTestData.uid == pk)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


# 모든 데이터 검색
async def find_all(db: AsyncSession):
    stmt = select(Db1TemplateTestData)
    result = await db.execute(stmt)
    return result.scalars().all()
