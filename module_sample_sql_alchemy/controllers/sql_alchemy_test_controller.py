from fastapi import APIRouter, Query, Path, Form, UploadFile, File, responses, Response, Request, Header, Body
from fastapi.responses import PlainTextResponse, HTMLResponse, StreamingResponse, FileResponse
from typing import Optional, List
import module_sample_sql_alchemy.services.api_test_service as service
import module_sample_sql_alchemy.models.api_test_model as model

# [그룹 컨트롤러]
# Router 설정
router = APIRouter(
    prefix="/sql-alchemy-test",  # 전체 경로 앞에 붙는 prefix
    tags=["SqlAlchemy 테스트 컨트롤러"]  # Swagger 문서 그룹 이름
)


# ----------------------------------------------------------------------------------------------------------------------
# <API 선언 공간>
@router.get(
    "",
    response_class=responses.PlainTextResponse,
    summary="기본 요청 테스트 API",
    description="이 API 를 요청하면 현재 실행중인 프로필 이름을 반환합니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def basic_request_test(
        request: Request,
        response: Response
):
    return await service.basic_request_test(request, response)
