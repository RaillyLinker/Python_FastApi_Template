from sqlalchemy import select, text, DateTime, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect
import tzlocal
import module_sample_sql_alchemy.utils.sql_alchemy_util as sql_alchemy_util
import module_sample_sql_alchemy.sql_alchemy_objects.db1_main.value_objects.template_test_data_vo as value_objects
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_test_data import Db1TemplateTestData
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import db_timezone
from typing import List, Sequence, Optional, Tuple
from datetime import datetime
from sqlalchemy import func


# [SqlAlchemy 레포지토리]
# 데이터 변경 함수 사용시 commit, rollback 처리를 해주세요.

# 데이터 save(동일 pk 가 존재 하면 update, 없다면 insert)
async def save(db: AsyncSession, entity: Db1TemplateTestData) -> Db1TemplateTestData:
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
async def find_all(db: AsyncSession) -> Sequence[Db1TemplateTestData]:
    stmt = select(Db1TemplateTestData)
    result = await db.execute(stmt)
    entity_list = result.scalars().all()
    # Entity 안의 datetime 에 타임존 정보 입력
    sql_alchemy_util.apply_timezone_to_datetime_fields_in_list(entity_list, db_timezone)
    return entity_list


# 데이터 pk 로 검색(0 or 1 result)
async def find_by_id(db: AsyncSession, pk: int) -> Optional[Db1TemplateTestData]:
    stmt = select(Db1TemplateTestData).where(Db1TemplateTestData.uid == pk)
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    # Entity 안의 datetime 에 타임존 정보 입력
    sql_alchemy_util.apply_timezone_to_datetime_fields(entity, db_timezone)
    return entity


# ---- (커스텀 쿼리 함수 추가 공간) ----
# (데이터 pk 로 검색(0 or 1 result))
async def find_by_uid_and_row_delete_date_str(
        db: AsyncSession,
        pk: int,
        row_delete_date_str: str
) -> Optional[Db1TemplateTestData]:
    stmt = select(Db1TemplateTestData).where(
        Db1TemplateTestData.uid == pk and
        Db1TemplateTestData.row_delete_date_str == row_delete_date_str
    )
    result = await db.execute(stmt)
    entity = result.scalar_one_or_none()
    # Entity 안의 datetime 에 타임존 정보 입력
    sql_alchemy_util.apply_timezone_to_datetime_fields(entity, db_timezone)
    return entity


# (입력값 거리 측정 쿼리)
async def find_all_by_not_deleted_with_random_distance(
        db: AsyncSession,
        num: int
) -> List[value_objects.FindAllFromTemplateTestDataByNotDeletedWithRandomNumDistanceOutputVo]:
    query = text("""
            SELECT 
            test_data.uid AS uid, 
            test_data.row_create_date AS rowCreateDate, 
            test_data.row_update_date AS rowUpdateDate, 
            test_data.content AS content, 
            test_data.random_num AS randomNum, 
            test_data.test_datetime AS testDatetime, 
            ABS(test_data.random_num-:num) AS distance 
            FROM 
            template.test_data AS test_data 
            WHERE 
            test_data.row_delete_date_str = '/' 
            ORDER BY 
            distance
    """)

    result = await db.execute(query, {"num": num})
    rows = result.mappings().all()  # key-value dict로 가져옴

    output = [
        value_objects.FindAllFromTemplateTestDataByNotDeletedWithRandomNumDistanceOutputVo(
            uid=row["uid"],
            row_create_date=row["rowCreateDate"].astimezone(db_timezone),
            row_update_date=row["rowUpdateDate"].astimezone(db_timezone),
            content=row["content"],
            random_num=row["randomNum"],
            test_datetime=row["testDatetime"].astimezone(db_timezone),
            distance=row["distance"]
        )
        for row in rows
    ]

    return output


# ----
# (입력 date 값 거리 측정 쿼리)
async def find_all_from_template_test_data_by_not_deleted_with_row_create_date_distance(
        db: AsyncSession,
        date: datetime
) -> List[value_objects.FindAllFromTemplateTestDataByNotDeletedWithRowCreateDateDistanceOutputVo]:
    query = text("""
            SELECT 
            test_data.uid AS uid, 
            test_data.content AS content, 
            test_data.random_num AS randomNum, 
            test_data.test_datetime AS testDatetime, 
            test_data.row_create_date AS rowCreateDate, 
            test_data.row_update_date AS rowUpdateDate, 
            ABS(TIMESTAMPDIFF(MICROSECOND, test_data.row_create_date, :date)) AS timeDiffMicroSec 
            FROM 
            template.test_data AS test_data 
            WHERE 
            test_data.row_delete_date_str = '/' 
            ORDER BY 
            timeDiffMicroSec
    """)

    result = await db.execute(query, {"date": date})
    rows = result.mappings().all()  # key-value dict로 가져옴

    output = [
        value_objects.FindAllFromTemplateTestDataByNotDeletedWithRowCreateDateDistanceOutputVo(
            uid=row["uid"],
            row_create_date=row["rowCreateDate"].astimezone(db_timezone),
            row_update_date=row["rowUpdateDate"].astimezone(db_timezone),
            content=row["content"],
            random_num=row["randomNum"],
            test_datetime=row["testDatetime"].astimezone(db_timezone),
            time_diff_micro_sec=row["timeDiffMicroSec"]
        )
        for row in rows
    ]

    return output


# ----
# (페이지네이션 샘플)
async def find_all_by_row_delete_date_str_order_by_row_create_date(
        db: AsyncSession,
        page: int,
        page_elements_count: int
) -> Tuple[Sequence[Db1TemplateTestData], int]:
    offset = (page - 1) * page_elements_count

    # 필터링 + 정렬 + 페이지네이션
    result = await db.execute(
        select(Db1TemplateTestData)
        .where(Db1TemplateTestData.row_delete_date_str == "/")
        .order_by(Db1TemplateTestData.row_create_date)
        .offset(offset)
        .limit(page_elements_count)
    )
    entities = result.scalars().all()

    # 총 개수 계산
    count_result = await db.execute(
        select(func.count(Db1TemplateTestData.uid))
        .where(Db1TemplateTestData.row_delete_date_str == "/")
    )
    total_elements = count_result.scalar_one()

    return entities, total_elements


# ----
# (네이티브 페이지네이션 샘플)
async def find_page_all_from_template_test_data_by_not_deleted_with_random_num_distance(
        db: AsyncSession,
        page: int,
        page_elements_count: int,
        num: int
) -> Tuple[List[value_objects.FindPageAllFromTemplateTestDataByNotDeletedWithRandomNumDistanceOutputVo], int]:
    offset = (page - 1) * page_elements_count

    # 본문 조회 (distance 기준 정렬)
    result = await db.execute(
        text("""
            SELECT 
                test_data.uid AS uid,
                test_data.row_create_date AS row_create_date,
                test_data.row_update_date AS row_update_date,
                test_data.content AS content,
                test_data.random_num AS random_num,
                test_data.test_datetime AS test_datetime,
                ABS(test_data.random_num - :num) AS distance
            FROM 
                template.test_data AS test_data
            WHERE 
                test_data.row_delete_date_str = '/'
            ORDER BY 
                distance
            LIMIT :limit OFFSET :offset
        """),
        {"num": num, "limit": page_elements_count, "offset": offset}
    )

    rows = result.mappings().all()

    entities = [
        value_objects.FindPageAllFromTemplateTestDataByNotDeletedWithRandomNumDistanceOutputVo(
            uid=row["uid"],
            row_create_date=row["row_create_date"],
            row_update_date=row["row_update_date"],
            content=row["content"],
            random_num=row["random_num"],
            test_datetime=row["test_datetime"],
            distance=row["distance"]
        )
        for row in rows
    ]

    # 총 개수 조회
    count_result = await db.execute(
        text("""
            SELECT 
                COUNT(*) 
            FROM 
                template.test_data AS test_data
            WHERE 
                test_data.row_delete_date_str = '/'
        """)
    )
    total_elements = count_result.scalar_one()

    return entities, total_elements


# ----
# (네이티브 데이터 수정 샘플)
async def update_to_template_test_data_set_content_and_test_date_time_by_uid(
        db: AsyncSession,
        uid: int,
        content: str,
        test_datetime: datetime
):
    await db.execute(
        text("""
            UPDATE 
            template.test_data 
            SET 
            content = :content, 
            test_datetime = :testDatetime 
            WHERE 
            uid = :uid
        """),
        {
            "uid": uid,
            "content": content,
            "testDatetime": test_datetime
        }
    )


# ----
# (ORM 데이터 수정 샘플)
async def update_to_template_test_data_set_content_and_test_date_time_by_uid_orm(
        db: AsyncSession,
        uid: int,
        content: str,
        test_datetime: datetime
):
    stmt = (
        update(Db1TemplateTestData)
        .where(Db1TemplateTestData.uid == uid)
        .values(
            content=content,
            test_datetime=test_datetime
        )
    )
    await db.execute(stmt)


# ----
# (키워드 검색 샘플)
async def find_page_all_from_template_test_data_by_search_keyword(
        db: AsyncSession,
        page: int,
        page_elements_count: int,
        search_keyword: str
) -> Tuple[List[value_objects.FindPageAllFromTemplateTestDataBySearchKeywordOutputVo], int]:
    offset = (page - 1) * page_elements_count

    # 본문 조회 (검색 키워드 기반)
    result = await db.execute(
        text("""
            SELECT 
                test_data.uid AS uid,
                test_data.row_create_date AS row_create_date,
                test_data.row_update_date AS row_update_date,
                test_data.content AS content,
                test_data.random_num AS random_num,
                test_data.test_datetime AS test_datetime
            FROM 
                template.test_data AS test_data
            WHERE 
                REPLACE(test_data.content, ' ', '') LIKE REPLACE(CONCAT('%', :search_keyword, '%'), ' ', '')
                AND test_data.row_delete_date_str = '/'
            ORDER BY 
                test_data.row_create_date DESC
            LIMIT :limit OFFSET :offset
        """),
        {"search_keyword": search_keyword, "limit": page_elements_count, "offset": offset}
    )

    rows = result.mappings().all()

    entities = [
        value_objects.FindPageAllFromTemplateTestDataBySearchKeywordOutputVo(
            uid=row["uid"],
            row_create_date=row["row_create_date"],
            row_update_date=row["row_update_date"],
            content=row["content"],
            random_num=row["random_num"],
            test_datetime=row["test_datetime"]
        )
        for row in rows
    ]

    # 총 개수 조회
    count_result = await db.execute(
        text("""
            SELECT 
                COUNT(*)
            FROM 
                template.test_data AS test_data
            WHERE 
                REPLACE(test_data.content, ' ', '') LIKE REPLACE(CONCAT('%', :search_keyword, '%'), ' ', '')
                AND test_data.row_delete_date_str = '/'
        """),
        {"search_keyword": search_keyword}
    )
    total_elements = count_result.scalar_one()

    return entities, total_elements
