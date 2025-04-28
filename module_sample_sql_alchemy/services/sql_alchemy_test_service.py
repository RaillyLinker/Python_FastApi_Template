import random
from datetime import datetime
from fastapi import Response, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
import tzlocal
from typing import List
import module_sample_sql_alchemy.utils.custom_util as custom_util
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import sql_alchemy_transactional
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_test_data import Db1TemplateTestData
import module_sample_sql_alchemy.models.sql_alchemy_test_model as model
import module_sample_sql_alchemy.sql_alchemy_objects.db1_main.repositories.template_test_data_repository \
    as template_test_data_repository
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_logical_delete_unique_data import \
    Db1TemplateLogicalDeleteUniqueData
import module_sample_sql_alchemy.sql_alchemy_objects.db1_main.repositories.template_local_delete_unique_data_repository \
    as template_local_delete_unique_data_repository


# [그룹 서비스]
# (DB Row 입력 테스트 API)
@sql_alchemy_transactional()
async def post_insert_data_sample(
        request: Request,
        response: Response,
        request_body: model.PostInsertDataSampleInputVo,
        db: AsyncSession
):
    # yyyy_MM_dd_'T'_HH_mm_ss_SSS_z 형식 string -> datetime
    datetime_obj = custom_util.parse_custom_datetime(request_body.date_string, "yyyy_MM_dd_'T'_HH_mm_ss_SSS_z")

    # 데이터 저장
    now_datetime = datetime.now()
    new_entity = await template_test_data_repository.save(
        db,
        Db1TemplateTestData(
            row_create_date=now_datetime,
            row_update_date=now_datetime,
            row_delete_date_str="/",
            content=request_body.content,
            random_num=random.randint(0, 99999999),
            test_datetime=datetime_obj
        )
    )

    return JSONResponse(
        status_code=200,
        content=model.PostInsertDataSampleOutputVo(
            uid=new_entity.uid,
            create_date=
            new_entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_create_date.microsecond // 1000:03d}"
            f"_{new_entity.row_create_date.tzname()}",
            update_date=
            new_entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_update_date.microsecond // 1000:03d}"
            f"_{new_entity.row_update_date.tzname()}",
            delete_date=new_entity.row_delete_date_str,
            content=new_entity.content,
            random_num=new_entity.random_num,
            test_datetime=
            new_entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.test_datetime.microsecond // 1000:03d}"
            f"_{new_entity.test_datetime.tzname()}",
        ).model_dump()
    )


# ----
# (DB Rows 삭제 테스트 API)
@sql_alchemy_transactional()
async def delete_rows_sample(
        request: Request,
        response: Response,
        delete_logically: bool,
        db: AsyncSession
):
    if delete_logically:
        entity_list = await template_test_data_repository.find_all(db)
        for entity in entity_list:
            if entity.row_delete_date_str != "/":
                continue

            now_datetime = datetime.now().replace(tzinfo=tzlocal.get_localzone())
            entity.row_delete_date_str = \
                (now_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
                 f"_{now_datetime.microsecond // 1000:03d}" +
                 f"_{now_datetime.tzname()}")
            await template_test_data_repository.save(db, entity)
    else:
        await template_test_data_repository.delete_all(db)

    return Response(
        status_code=200
    )


# ----
# (DB Row 삭제 테스트 API)
@sql_alchemy_transactional()
async def delete_row_sample(
        request: Request,
        response: Response,
        index: int,
        delete_logically: bool,
        db: AsyncSession
):
    entity = await template_test_data_repository.find_by_id(db, index)

    if entity is None:
        return Response(
            status_code=204,
            headers={"api-result-code": "1"}
        )

    if delete_logically:
        if entity.row_delete_date_str != "/":
            return Response(
                status_code=204,
                headers={"api-result-code": "1"}
            )

        now_datetime = datetime.now().replace(tzinfo=tzlocal.get_localzone())
        entity.row_delete_date_str = \
            (now_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
             f"_{now_datetime.microsecond // 1000:03d}" +
             f"_{now_datetime.tzname()}")
        await template_test_data_repository.save(db, entity)
    else:
        await template_test_data_repository.delete_by_id(db, index)

    return Response(
        status_code=200
    )


# ----
# (DB Rows 조회 테스트 API)
@sql_alchemy_transactional(view_only=True)
async def get_rows(
        request: Request,
        response: Response,
        db: AsyncSession
):
    entity_list = await template_test_data_repository.find_all(db)

    test_entity_vo_list: List[model.GetSelectRowsSampleOutputVo.TestEntityVo] = []
    logical_delete_entity_vo_list: List[model.GetSelectRowsSampleOutputVo.TestEntityVo] = []

    for entity in entity_list:
        entity_output = model.GetSelectRowsSampleOutputVo.TestEntityVo(
            uid=entity.uid,
            create_date=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            update_date=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            delete_date=entity.row_delete_date_str,
            content=entity.content,
            random_num=entity.random_num,
            test_datetime=
            entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.test_datetime.microsecond // 1000:03d}"
            f"_{entity.test_datetime.tzname()}",
        )

        if entity.row_delete_date_str == "/":
            # 논리 삭제되지 않은 데이터
            test_entity_vo_list.append(entity_output)
        else:
            # 논리 삭제된 데이터
            logical_delete_entity_vo_list.append(entity_output)

    return JSONResponse(
        status_code=200,
        content=model.GetSelectRowsSampleOutputVo(
            test_entity_vo_list=test_entity_vo_list,
            logical_delete_entity_vo_list=logical_delete_entity_vo_list
        ).model_dump()
    )


# ----
# (DB 테이블의 random_num 컬럼 근사치 기준으로 정렬한 리스트 조회 API)
@sql_alchemy_transactional(view_only=True)
async def get_rows_order_by_random_num_sample(
        request: Request,
        response: Response,
        num: int,
        db: AsyncSession
):
    entity_list = await template_test_data_repository.find_all_by_not_deleted_with_random_distance(db, num)

    test_entity_vo_list: List[model.GetRowsOrderByRandomNumSampleOutputVo.TestEntityVo] = []

    for entity in entity_list:
        entity_output = model.GetRowsOrderByRandomNumSampleOutputVo.TestEntityVo(
            uid=entity.uid,
            create_date=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            update_date=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            content=entity.content,
            random_num=entity.random_num,
            test_datetime=
            entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.test_datetime.microsecond // 1000:03d}"
            f"_{entity.test_datetime.tzname()}",
            distance=entity.distance
        )

        test_entity_vo_list.append(entity_output)

    return JSONResponse(
        status_code=200,
        content=model.GetRowsOrderByRandomNumSampleOutputVo(
            test_entity_vo_list=test_entity_vo_list
        ).model_dump()
    )


# ----
# (DB 테이블의 row_create_date 컬럼 근사치 기준으로 정렬한 리스트 조회 API)
@sql_alchemy_transactional(view_only=True)
async def get_rows_order_by_row_create_date_sample(
        request: Request,
        response: Response,
        date_string: str,
        db: AsyncSession
):
    # yyyy_MM_dd_'T'_HH_mm_ss_SSS_z 형식 string -> datetime
    datetime_obj = custom_util.parse_custom_datetime(date_string, "yyyy_MM_dd_'T'_HH_mm_ss_SSS_z")

    entity_list = await template_test_data_repository.find_all_from_template_test_data_by_not_deleted_with_row_create_date_distance(
        db,
        datetime_obj
    )

    test_entity_vo_list: List[model.GetRowsOrderByRowCreateDateSampleOutputVo.TestEntityVo] = []

    for entity in entity_list:
        entity_output = model.GetRowsOrderByRowCreateDateSampleOutputVo.TestEntityVo(
            uid=entity.uid,
            create_date=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            update_date=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            content=entity.content,
            random_num=entity.random_num,
            test_datetime=
            entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.test_datetime.microsecond // 1000:03d}"
            f"_{entity.test_datetime.tzname()}",
            time_diff_micro_sec=entity.time_diff_micro_sec
        )

        test_entity_vo_list.append(entity_output)

    return JSONResponse(
        status_code=200,
        content=model.GetRowsOrderByRowCreateDateSampleOutputVo(
            test_entity_vo_list=test_entity_vo_list
        ).model_dump()
    )


# ----
# (DB Rows 조회 테스트 (페이징))
@sql_alchemy_transactional(view_only=True)
async def get_rows_page_sample(
        request: Request,
        response: Response,
        page: int,
        page_elements_count: int,
        db: AsyncSession
):
    entities, total_elements = await template_test_data_repository.find_all_by_row_delete_date_str_order_by_row_create_date(
        db,
        page,
        page_elements_count
    )

    # 엔티티 -> VO 매핑
    test_entity_vo_list = [
        model.GetRowsPageSampleOutputVo.TestEntityVo(
            uid=entity.uid,
            createDate=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            updateDate=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            content=entity.content,
            randomNum=entity.random_num,
            testDatetime=
            entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.test_datetime.microsecond // 1000:03d}"
            f"_{entity.test_datetime.tzname()}"
        )
        for entity in entities
    ]

    return JSONResponse(
        status_code=200,
        content=model.GetRowsPageSampleOutputVo(
            total_elements=total_elements,
            test_entity_vo_list=test_entity_vo_list
        ).model_dump()
    )


# ----
# (DB Rows 조회 테스트 (네이티브 쿼리 페이징))
@sql_alchemy_transactional(view_only=True)
async def get_rows_native_query_page_sample(
        request: Request,
        response: Response,
        page: int,
        page_elements_count: int,
        num: int,
        db: AsyncSession
):
    entities, total_elements = await template_test_data_repository.find_page_all_from_template_test_data_by_not_deleted_with_random_num_distance(
        db,
        page,
        page_elements_count,
        num
    )

    # 엔티티 -> VO 매핑
    test_entity_vo_list = [
        model.GetRowsNativeQueryPageSampleOutputVo.TestEntityVo(
            uid=entity.uid,
            createDate=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            updateDate=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            content=entity.content,
            randomNum=entity.random_num,
            testDatetime=
            entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.test_datetime.microsecond // 1000:03d}"
            f"_{entity.test_datetime.tzname()}",
            distance=entity.distance
        )
        for entity in entities
    ]

    return JSONResponse(
        status_code=200,
        content=model.GetRowsNativeQueryPageSampleOutputVo(
            total_elements=total_elements,
            test_entity_vo_list=test_entity_vo_list
        ).model_dump()
    )


# ----
# (DB Row 수정 테스트 API)
@sql_alchemy_transactional()
async def put_row_sample(
        request: Request,
        response: Response,
        test_table_uid: int,
        request_body: model.PutRowSampleInputVo,
        db: AsyncSession
):
    entity = await template_test_data_repository.find_by_uid_and_row_delete_date_str(db, test_table_uid, "/")

    if entity is None:
        return Response(
            status_code=204,
            headers={"api-result-code": "1"}
        )

    entity.content = request_body.content

    # yyyy_MM_dd_'T'_HH_mm_ss_SSS_z 형식 string -> datetime
    datetime_obj = custom_util.parse_custom_datetime(request_body.date_string, "yyyy_MM_dd_'T'_HH_mm_ss_SSS_z")
    entity.test_datetime = datetime_obj

    now_datetime = datetime.now()
    entity.row_update_date = now_datetime

    # 데이터 저장
    new_entity = await template_test_data_repository.save(db, entity)

    return JSONResponse(
        status_code=200,
        content=model.PutRowSampleOutputVo(
            uid=new_entity.uid,
            create_date=
            new_entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_create_date.microsecond // 1000:03d}"
            f"_{new_entity.row_create_date.tzname()}",
            update_date=
            new_entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_update_date.microsecond // 1000:03d}"
            f"_{new_entity.row_update_date.tzname()}",
            content=new_entity.content,
            random_num=new_entity.random_num,
            test_datetime=
            new_entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.test_datetime.microsecond // 1000:03d}"
            f"_{new_entity.test_datetime.tzname()}",
        ).model_dump()
    )


# ----
# (DB Row 수정 테스트 (ORM))
@sql_alchemy_transactional()
async def put_row_orm_sample(
        request: Request,
        response: Response,
        test_table_uid: int,
        request_body: model.PutRowOrmSampleInputVo,
        db: AsyncSession
):
    entity = await template_test_data_repository.find_by_uid_and_row_delete_date_str(db, test_table_uid, "/")

    if entity is None:
        return Response(
            status_code=204,
            headers={"api-result-code": "1"}
        )

    # yyyy_MM_dd_'T'_HH_mm_ss_SSS_z 형식 string -> datetime
    datetime_obj = custom_util.parse_custom_datetime(request_body.date_string, "yyyy_MM_dd_'T'_HH_mm_ss_SSS_z")

    # 데이터 수정
    await template_test_data_repository.update_to_template_test_data_set_content_and_test_date_time_by_uid_orm(
        db,
        test_table_uid,
        request_body.content,
        datetime_obj
    )

    return Response(
        status_code=200
    )


# ----
# (DB Rows 조회 테스트 (네이티브 쿼리 페이징))
@sql_alchemy_transactional(view_only=True)
async def get_row_where_searching_keyword_sample(
        request: Request,
        response: Response,
        page: int,
        page_elements_count: int,
        search_keyword: str,
        db: AsyncSession
):
    entities, total_elements = await template_test_data_repository.find_page_all_from_template_test_data_by_search_keyword(
        db,
        page,
        page_elements_count,
        search_keyword
    )

    # 엔티티 -> VO 매핑
    test_entity_vo_list = [
        model.GetRowWhereSearchingKeywordSampleOutputVo.TestEntityVo(
            uid=entity.uid,
            createDate=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            updateDate=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            content=entity.content,
            randomNum=entity.random_num,
            testDatetime=
            entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.test_datetime.microsecond // 1000:03d}"
            f"_{entity.test_datetime.tzname()}"
        )
        for entity in entities
    ]

    return JSONResponse(
        status_code=200,
        content=model.GetRowWhereSearchingKeywordSampleOutputVo(
            total_elements=total_elements,
            test_entity_vo_list=test_entity_vo_list
        ).model_dump()
    )


# ----
# (트랜젝션 동작 테스트)
@sql_alchemy_transactional()
async def post_transaction_test(
        request: Request,
        response: Response,
        db: AsyncSession
):
    # 데이터 저장
    now_datetime = datetime.now()
    await template_test_data_repository.save(
        db,
        Db1TemplateTestData(
            row_create_date=now_datetime,
            row_update_date=now_datetime,
            row_delete_date_str="/",
            content="error test",
            random_num=random.randint(0, 99999999),
            test_datetime=now_datetime
        )
    )

    raise Exception("Transaction Rollback Test!")


# ----
# (트랜젝션 비동작 테스트(try-catch))
@sql_alchemy_transactional()
async def post_try_transaction_test(
        request: Request,
        response: Response,
        db: AsyncSession
):
    try:
        # 데이터 저장
        now_datetime = datetime.now()
        await template_test_data_repository.save(
            db,
            Db1TemplateTestData(
                row_create_date=now_datetime,
                row_update_date=now_datetime,
                row_delete_date_str="/",
                content="error test",
                random_num=random.randint(0, 99999999),
                test_datetime=now_datetime
            )
        )

        raise Exception("Transaction Rollback Test!")
    except Exception as e:
        print(e)


# ----
# (DB Rows 조회 테스트 (카운팅))
@sql_alchemy_transactional(view_only=True)
async def get_rows_count_sample(
        request: Request,
        response: Response,
        db: AsyncSession
):
    entity_count = await template_test_data_repository.count_by_row_delete_date_str(
        db,
        "/"
    )

    return JSONResponse(
        status_code=200,
        content=model.GetRowsCountSampleOutputVo(
            total_elements=entity_count
        ).model_dump()
    )


# ----
# (DB Rows 조회 테스트 (네이티브 카운팅))
@sql_alchemy_transactional(view_only=True)
async def get_rows_count_by_native_query_sample(
        request: Request,
        response: Response,
        db: AsyncSession
):
    entity_count = await template_test_data_repository.count_from_template_test_data_by_not_deleted(
        db,
        "/"
    )

    return JSONResponse(
        status_code=200,
        content=model.GetRowsCountByNativeQuerySample(
            total_elements=entity_count
        ).model_dump()
    )


# ----
# (DB Row 조회 테스트 (네이티브))
@sql_alchemy_transactional(view_only=True)
async def get_row_by_native_query_sample(
        request: Request,
        response: Response,
        test_table_uid: int,
        db: AsyncSession
):
    entity = await template_test_data_repository.find_by_id(db, test_table_uid)

    if entity is None:
        return Response(
            status_code=204,
            headers={"api-result-code": "1"}
        )

    return JSONResponse(
        status_code=200,
        content=model.PostInsertDataSampleOutputVo(
            uid=entity.uid,
            create_date=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            update_date=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            delete_date=entity.row_delete_date_str,
            content=entity.content,
            random_num=entity.random_num,
            test_datetime=
            entity.test_datetime.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.test_datetime.microsecond // 1000:03d}"
            f"_{entity.test_datetime.tzname()}",
        ).model_dump()
    )


# ----
# (유니크 테스트 테이블 Row 입력 API)
@sql_alchemy_transactional()
async def post_unique_test_table_row_sample(
        request: Request,
        response: Response,
        request_body: model.PostUniqueTestTableRowSampleInputVo,
        db: AsyncSession
):
    # 데이터 저장
    now_datetime = datetime.now()
    new_entity = await template_local_delete_unique_data_repository.save(
        db,
        Db1TemplateLogicalDeleteUniqueData(
            row_create_date=now_datetime,
            row_update_date=now_datetime,
            row_delete_date_str="/",
            unique_value=request_body.unique_value
        )
    )

    return JSONResponse(
        status_code=200,
        content=model.PostUniqueTestTableRowSampleOutputVo(
            uid=new_entity.uid,
            create_date=
            new_entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_create_date.microsecond // 1000:03d}"
            f"_{new_entity.row_create_date.tzname()}",
            update_date=
            new_entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_update_date.microsecond // 1000:03d}"
            f"_{new_entity.row_update_date.tzname()}",
            delete_date=new_entity.row_delete_date_str,
            unique_value=new_entity.unique_value
        ).model_dump()
    )


# ----
# (유니크 테스트 테이블 Rows 조회 테스트)
@sql_alchemy_transactional()
async def get_unique_test_table_rows_sample(
        request: Request,
        response: Response,
        db: AsyncSession
):
    entity_list = await template_local_delete_unique_data_repository.find_all(db)

    test_entity_vo_list: List[model.GetUniqueTestTableRowsSampleOutputVo.TestEntityVo] = []
    logical_delete_entity_vo_list: List[model.GetUniqueTestTableRowsSampleOutputVo.TestEntityVo] = []

    for entity in entity_list:
        entity_output = model.GetUniqueTestTableRowsSampleOutputVo.TestEntityVo(
            uid=entity.uid,
            create_date=
            entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_create_date.microsecond // 1000:03d}"
            f"_{entity.row_create_date.tzname()}",
            update_date=
            entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{entity.row_update_date.microsecond // 1000:03d}"
            f"_{entity.row_update_date.tzname()}",
            delete_date=entity.row_delete_date_str,
            unique_value=entity.unique_value
        )

        if entity.row_delete_date_str == "/":
            # 논리 삭제되지 않은 데이터
            test_entity_vo_list.append(entity_output)
        else:
            # 논리 삭제된 데이터
            logical_delete_entity_vo_list.append(entity_output)

    return JSONResponse(
        status_code=200,
        content=model.GetUniqueTestTableRowsSampleOutputVo(
            test_entity_vo_list=test_entity_vo_list,
            logical_delete_entity_vo_list=logical_delete_entity_vo_list
        ).model_dump()
    )


# ----
# (유니크 테스트 테이블 Row 수정 테스트)
@sql_alchemy_transactional()
async def put_unique_test_table_row_sample(
        request: Request,
        response: Response,
        unique_test_table_uid: int,
        request_body: model.PutUniqueTestTableRowSampleInputVo,
        db: AsyncSession
):
    entity = await template_local_delete_unique_data_repository.find_by_id(db, unique_test_table_uid)

    if entity is None or entity.row_delete_date_str != "/":
        return Response(
            status_code=204,
            headers={"api-result-code": "1"}
        )

    u_entity = await template_local_delete_unique_data_repository.find_by_unique_value_and_row_delete_date_str(
        db,
        request_body.unique_value,
        "/"
    )

    if u_entity is not None:
        return Response(
            status_code=204,
            headers={"api-result-code": "2"}
        )

    # 데이터 수정
    entity.unique_value = request_body.unique_value
    now_datetime = datetime.now()
    entity.row_update_date = now_datetime

    # 데이터 저장
    new_entity = await template_local_delete_unique_data_repository.save(db, entity)

    return JSONResponse(
        status_code=200,
        content=model.PutUniqueTestTableRowSampleOutputVo(
            uid=new_entity.uid,
            create_date=
            new_entity.row_create_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_create_date.microsecond // 1000:03d}"
            f"_{new_entity.row_create_date.tzname()}",
            update_date=
            new_entity.row_update_date.strftime('%Y_%m_%d_T_%H_%M_%S') +
            f"_{new_entity.row_update_date.microsecond // 1000:03d}"
            f"_{new_entity.row_update_date.tzname()}",
            unique_value=new_entity.unique_value
        ).model_dump()
    )
