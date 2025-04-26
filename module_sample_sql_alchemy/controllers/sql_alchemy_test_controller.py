from fastapi import APIRouter, Response, Request, Body, Query, Path
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


# ----
@router.delete(
    "/rows",
    summary="DB Rows 삭제 테스트 API",
    description="테스트 테이블의 모든 Row 를 모두 삭제합니다.",
    responses={
        200: {
            "description": "OK",
            "content": {"*/*": {}}
        }
    },
    response_class=Response
)
async def delete_rows_sample(
        request: Request,
        response: Response,
        delete_logically: bool =
        Query(
            ...,
            alias="deleteLogically",
            description="논리적 삭제 여부",
            example=True
        )
):
    return await service.delete_rows_sample(
        request,
        response,
        delete_logically
    )


# ----
@router.delete(
    "/row/{index}",
    summary="DB Row 삭제 테스트 API",
    description="테스트 테이블의 Row 하나를 삭제합니다.",
    responses={
        200: {
            "description": "OK",
            "content": {"*/*": {}}
        },
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : index 에 해당하는 데이터가 데이터베이스에 존재하지 않습니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    },
    response_class=Response
)
async def delete_row_sample(
        request: Request,
        response: Response,
        index: int = Path(
            ...,
            alias="index",
            description="글 인덱스",
            example=1
        ),
        delete_logically: bool =
        Query(
            ...,
            alias="deleteLogically",
            description="논리적 삭제 여부",
            example=True
        )
):
    return await service.delete_row_sample(
        request,
        response,
        index,
        delete_logically
    )


# ----
@router.get(
    "/rows",
    response_model=model.GetSelectRowsSampleOutputVo,
    summary="DB Rows 조회 테스트 API",
    description="테스트 테이블의 모든 Rows 를 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_rows(
        request: Request,
        response: Response
):
    return await service.get_rows(
        request,
        response
    )


# ----
@router.get(
    "/rows/order-by-random-num-nearest",
    response_model=model.GetRowsOrderByRandomNumSampleOutputVo,
    summary="DB 테이블의 random_num 컬럼 근사치 기준으로 정렬한 리스트 조회 API",
    description="테이블의 row 중 random_num 컬럼과 num 파라미터의 값의 근사치로 정렬한 리스트 반환",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_rows_order_by_random_num_sample(
        request: Request,
        response: Response,
        num: int =
        Query(
            ...,
            alias="num",
            description="근사값 정렬의 기준",
            example=1
        )
):
    return await service.get_rows_order_by_random_num_sample(
        request,
        response,
        num
    )


# ----
@router.get(
    "/rows/order-by-create-date-nearest",
    response_model=model.GetRowsOrderByRowCreateDateSampleOutputVo,
    summary="DB 테이블의 row_create_date 컬럼 근사치 기준으로 정렬한 리스트 조회 API",
    description="테이블의 row 중 row_create_date 컬럼과 dateString 파라미터의 값의 근사치로 정렬한 리스트 반환",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_rows_order_by_row_create_date_sample(
        request: Request,
        response: Response,
        date_string: str =
        Query(
            ...,
            alias="dateString",
            description="원하는 날짜(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            example="2024_05_02_T_15_14_49_552_KST"
        )
):
    return await service.get_rows_order_by_row_create_date_sample(
        request,
        response,
        date_string
    )


# ----
@router.get(
    "/rows/paging",
    response_model=model.GetRowsPageSampleOutputVo,
    summary="DB Rows 조회 테스트 (페이징)",
    description="테스트 테이블의 Rows 를 페이징하여 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_rows_page_sample(
        request: Request,
        response: Response,
        page: int =
        Query(
            ...,
            alias="page",
            description="원하는 페이지(1부터 시작)",
            example=1
        ),
        page_elements_count: int =
        Query(
            ...,
            alias="pageElementsCount",
            description="페이지 아이템 개수",
            example=10
        )
):
    return await service.get_rows_page_sample(
        request,
        response,
        page,
        page_elements_count
    )


# ----
@router.get(
    "/rows/native-paging",
    response_model=model.GetRowsNativeQueryPageSampleOutputVo,
    summary="DB Rows 조회 테스트 (네이티브 쿼리 페이징)",
    description="테스트 테이블의 Rows 를 네이티브 쿼리로 페이징하여 반환합니다.<br>"
                "num 을 기준으로 근사치 정렬도 수행합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_rows_native_query_page_sample(
        request: Request,
        response: Response,
        page: int =
        Query(
            ...,
            alias="page",
            description="원하는 페이지(1부터 시작)",
            example=1
        ),
        page_elements_count: int =
        Query(
            ...,
            alias="pageElementsCount",
            description="페이지 아이템 개수",
            example=10
        ),
        num: int =
        Query(
            ...,
            alias="num",
            description="근사값의 기준",
            example=1
        )
):
    return await service.get_rows_native_query_page_sample(
        request,
        response,
        page,
        page_elements_count,
        num
    )


# ----
@router.put(
    "/row/{testTableUid}",
    response_model=model.PutRowSampleOutputVo,
    summary="DB Row 수정 테스트 API",
    description="테스트 테이블의 Row 하나를 수정합니다.",
    responses={
        200: {"description": "OK"},
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : testTableUid 에 해당하는 정보가 데이터베이스에 존재하지 않습니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    }
)
async def put_row_sample(
        request: Request,
        response: Response,
        test_table_uid: int = Path(
            ...,
            alias="testTableUid",
            description="test 테이블의 uid",
            example=1
        ),
        request_body: model.PutRowSampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.put_row_sample(request, response, test_table_uid, request_body)


# ----
@router.put(
    "/row/{testTableUid}/native-query",
    summary="DB Row 수정 테스트 (네이티브 쿼리)",
    description="테스트 테이블의 Row 하나를 네이티브 쿼리로 수정합니다.",
    responses={
        200: {
            "description": "OK",
            "content": {"*/*": {}}
        },
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : testTableUid 에 해당하는 정보가 데이터베이스에 존재하지 않습니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    },
    response_class=Response
)
async def put_row_native_query_sample(
        request: Request,
        response: Response,
        test_table_uid: int = Path(
            ...,
            alias="testTableUid",
            description="test 테이블의 uid",
            example=1
        ),
        request_body: model.PutRowNativeQuerySampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.put_row_native_query_sample(request, response, test_table_uid, request_body)


# ----
@router.put(
    "/row/{testTableUid}/orm",
    summary="DB Row 수정 테스트 (ORM)",
    description="테스트 테이블의 Row 하나를 ORM 으로 수정합니다.",
    responses={
        200: {
            "description": "OK",
            "content": {"*/*": {}}
        },
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : testTableUid 에 해당하는 정보가 데이터베이스에 존재하지 않습니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    },
    response_class=Response
)
async def put_row_orm_sample(
        request: Request,
        response: Response,
        test_table_uid: int = Path(
            ...,
            alias="testTableUid",
            description="test 테이블의 uid",
            example=1
        ),
        request_body: model.PutRowOrmSampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.put_row_orm_sample(request, response, test_table_uid, request_body)
