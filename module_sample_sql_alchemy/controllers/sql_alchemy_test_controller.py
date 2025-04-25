from fastapi import APIRouter, Response, Request, Body
import module_sample_sql_alchemy.models.sql_alchemy_test_model as model
import module_sample_sql_alchemy.services.sql_alchemy_test_service as service

# [그룹 컨트롤러]
# Router 설정
router = APIRouter(
    prefix="/sql-alchemy-test",  # 전체 경로 앞에 붙는 prefix
    tags=["SqlAlchemy 테스트 컨트롤러"]  # Swagger 문서 그룹 이름
)


# ----------------------------------------------------------------------------------------------------------------------
# <API 선언 공간>
@router.post(
    "/row",
    response_model=model.PostInsertDataSampleOutputVo,
    summary="DB Row 입력 테스트 API",
    description="테스트 테이블에 Row 를 입력합니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def post_insert_data_sample(
        request: Request,
        response: Response,
        request_body: model.PostInsertDataSampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.post_insert_data_sample(request, response, request_body)
