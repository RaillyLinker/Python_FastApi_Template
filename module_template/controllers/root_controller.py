from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import module_template.services.root_service as service

# import module_template.models.root_service as model

# [그룹 컨트롤러]
# Router 설정
router = APIRouter(
    tags=["Root 경로에 대한 API 컨트롤러"]  # Swagger 문서 그룹 이름
)


# ----------------------------------------------------------------------------------------------------------------------
# <API 선언 공간>
@router.get(
    "/",
    response_class=HTMLResponse,
    summary="루트 경로",
    description="루트 경로 정보를 반환합니다."
)
async def get_root(
        request: Request
):
    return await service.get_root(request)


# ----
@router.get(
    "/favicon.ico",
    include_in_schema=False
)
async def get_favicon():
    return await service.get_favicon()
