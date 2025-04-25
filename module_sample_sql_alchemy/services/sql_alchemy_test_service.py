import random
from datetime import datetime, timezone, timedelta
from fastapi import Response, Request
from fastapi.responses import JSONResponse
import module_sample_sql_alchemy.models.sql_alchemy_test_model as model
import module_sample_sql_alchemy.sql_alchemy_objects.db1_main.repositories.template_test_data_repository \
    as template_test_data_repository
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import get_async_db
from module_sample_sql_alchemy.sql_alchemy_objects.db1_main.entities.template_test_data import Db1TemplateTestData
import module_sample_sql_alchemy.utils.custom_util as custom_util


# [그룹 서비스]
# (DB Row 입력 테스트 API)
async def post_insert_data_sample(
        request: Request,
        response: Response,
        request_body: model.PostInsertDataSampleInputVo
):
    async with get_async_db() as db:  # 여기가 중요
        try:
            # 문자열을 "_" 기준으로 나누기
            parts = request_body.date_string.split('_')

            # 각 요소 파싱
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            hour = int(parts[4])
            minute = int(parts[5])
            second = int(parts[6])
            microsecond = int(parts[7]) * 1000
            tzinfo = custom_util.get_timezone_from_str(parts[8])

            # datetime 객체 생성
            date_string = datetime(year, month, day, hour, minute, second, microsecond, tzinfo)

            new_entity = await template_test_data_repository.save(
                db,
                Db1TemplateTestData(
                    content=request_body.content,
                    random_num=random.randint(0, 99999999),
                    test_datetime=date_string
                )
            )

            await db.commit()

            return JSONResponse(
                status_code=200,
                content=model.PostInsertDataSampleOutputVo(
                    uid=new_entity.uid,
                    create_date="",
                    update_date="",
                    delete_date=new_entity.row_delete_date_str,
                    content=new_entity.content,
                    random_num=new_entity.random_num,
                    test_datetime=""
                ).model_dump()
            )
        except Exception as e:
            await db.rollback()
            raise e
