import random
from datetime import datetime
from fastapi import Response, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
import module_sample_sql_alchemy.models.sql_alchemy_test_model as model
import module_sample_sql_alchemy.sql_alchemy_objects.db1_main.repositories.template_test_data_repository \
    as template_test_data_repository
import module_sample_sql_alchemy.utils.custom_util as custom_util
import tzlocal
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import sql_alchemy_transactional, \
    sql_alchemy_transactional_view_only
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_test_data import Db1TemplateTestData
from typing import List


# [그룹 서비스]
# (DB Row 입력 테스트 API)
@sql_alchemy_transactional
async def post_insert_data_sample(
        request: Request,
        response: Response,
        request_body: model.PostInsertDataSampleInputVo,
        db: AsyncSession
):
    # yyyy_MM_dd_'T'_HH_mm_ss_SSS_z 형식 string -> datetime
    parts = request_body.date_string.split('_')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    hour = int(parts[4])
    minute = int(parts[5])
    second = int(parts[6])
    microsecond = int(parts[7]) * 1000
    tz_info = custom_util.get_timezone_from_str(parts[8])
    date_string = datetime(year, month, day, hour, minute, second, microsecond, tz_info)

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
            test_datetime=date_string
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
@sql_alchemy_transactional
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
@sql_alchemy_transactional
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
# (DB Row 삭제 테스트 API)
@sql_alchemy_transactional_view_only
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
@sql_alchemy_transactional_view_only
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
@sql_alchemy_transactional_view_only
async def get_rows_order_by_row_create_date_sample(
        request: Request,
        response: Response,
        date_string: str,
        db: AsyncSession
):
    # yyyy_MM_dd_'T'_HH_mm_ss_SSS_z 형식 string -> datetime
    parts = date_string.split('_')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    hour = int(parts[4])
    minute = int(parts[5])
    second = int(parts[6])
    microsecond = int(parts[7]) * 1000
    tz_info = custom_util.get_timezone_from_str(parts[8])
    datetime_obj = datetime(year, month, day, hour, minute, second, microsecond, tz_info)

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
