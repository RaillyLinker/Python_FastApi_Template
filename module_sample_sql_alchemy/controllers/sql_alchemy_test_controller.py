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


# ----
@router.get(
    "/search-content",
    response_model=model.GetRowWhereSearchingKeywordSampleOutputVo,
    summary="DB 정보 검색 테스트",
    description="글 본문 내용중 searchKeyword 가 포함된 rows 를 검색하여 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_row_where_searching_keyword_sample(
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
        search_keyword: str =
        Query(
            ...,
            alias="searchKeyword",
            description="검색어",
            example="테스트"
        )
):
    return await service.get_row_where_searching_keyword_sample(
        request,
        response,
        page,
        page_elements_count,
        search_keyword
    )


# ----
@router.post(
    "/transaction-rollback-sample",
    summary="트랜젝션 동작 테스트",
    description="정보 입력 후 Exception 이 발생했을 때 롤백되어 데이터가 저장되지 않는지를 테스트하는 API",
    responses={
        200: {
            "description": "OK",
            "content": {"*/*": {}}
        }
    },
    response_class=Response
)
async def post_transaction_test(
        request: Request,
        response: Response
):
    return await service.post_transaction_test(request, response)


# ----
@router.post(
    "/try-catch-no-transaction-exception-sample",
    summary="트랜젝션 비동작 테스트(try-catch)",
    description="에러 발생문이 try-catch 문 안에 있을 때, DB 정보 입력 후 Exception 이 발생 해도 트랜젝션이 동작하지 않는지에 대한 테스트 API",
    responses={
        200: {
            "description": "OK",
            "content": {"*/*": {}}
        }
    },
    response_class=Response
)
async def post_try_transaction_test(
        request: Request,
        response: Response
):
    return await service.post_try_transaction_test(request, response)


# ----
@router.get(
    "/rows/counting",
    response_model=model.GetRowsCountSampleOutputVo,
    summary="DB Rows 조회 테스트 (카운팅)",
    description="테스트 테이블의 Rows 를 카운팅하여 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_rows_count_sample(
        request: Request,
        response: Response
):
    return await service.get_rows_count_sample(
        request,
        response
    )


# ----
@router.get(
    "/rows/native-counting",
    response_model=model.GetRowsCountByNativeQuerySample,
    summary="DB Rows 조회 테스트 (네이티브 카운팅)",
    description="테스트 테이블의 Rows 를 네이티브 쿼리로 카운팅하여 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_rows_count_by_native_query_sample(
        request: Request,
        response: Response
):
    return await service.get_rows_count_by_native_query_sample(
        request,
        response
    )


# ----
@router.get(
    "/row/native/{testTableUid}",
    response_model=model.GetRowByNativeQuerySampleOutputVo,
    summary="DB Row 조회 테스트 (네이티브)",
    description="테스트 테이블의 Row 하나를 네이티브 쿼리로 반환합니다.",
    responses={
        200: {
            "description": "OK"
        },
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : testTableUid 에 해당하는 데이터가 데이터베이스에 존재하지 않습니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    }
)
async def get_row_by_native_query_sample(
        request: Request,
        response: Response,
        test_table_uid: int = Path(
            ...,
            alias="testTableUid",
            description="글 인덱스",
            example=1
        )
):
    return await service.get_row_by_native_query_sample(
        request,
        response,
        test_table_uid
    )


# ----
@router.post(
    "/unique-test-table",
    response_model=model.PostUniqueTestTableRowSampleOutputVo,
    summary="유니크 테스트 테이블 Row 입력 API",
    description="유니크 테스트 테이블에 Row 를 입력합니다.<br>"
                "논리적 삭제를 적용한 본 테이블에서 유니크 값은, 유니크 값 컬럼과 행 삭제일 데이터와의 혼합입니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def post_unique_test_table_row_sample(
        request: Request,
        response: Response,
        request_body: model.PostUniqueTestTableRowSampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.post_unique_test_table_row_sample(request, response, request_body)


# ----
@router.get(
    "/unique-test-table/all",
    response_model=model.GetUniqueTestTableRowsSampleOutputVo,
    summary="유니크 테스트 테이블 Rows 조회 테스트",
    description="유니크 테스트 테이블의 모든 Rows 를 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_unique_test_table_rows_sample(
        request: Request,
        response: Response
):
    return await service.get_unique_test_table_rows_sample(
        request,
        response
    )


# ----
@router.put(
    "/unique-test-table/{uniqueTestTableUid}",
    response_model=model.PutUniqueTestTableRowSampleOutputVo,
    summary="유니크 테스트 테이블 Row 수정 테스트",
    description="유니크 테스트 테이블의 Row 하나를 수정합니다.",
    responses={
        200: {"description": "OK"},
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : uniqueTestTableUid 에 해당하는 정보가 데이터베이스에 존재하지 않습니다.<br>"
                                   "2 : uniqueValue 와 일치하는 정보가 이미 데이터베이스에 존재합니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    }
)
async def put_unique_test_table_row_sample(
        request: Request,
        response: Response,
        unique_test_table_uid: int = Path(
            ...,
            alias="uniqueTestTableUid",
            description="test 테이블의 uid",
            example=1
        ),
        request_body: model.PutUniqueTestTableRowSampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.put_unique_test_table_row_sample(request, response, unique_test_table_uid, request_body)


# ----
@router.delete(
    "/unique-test-table/{index}",
    summary="유니크 테스트 테이블 Row 삭제 테스트",
    description="유니크 테스트 테이블의 Row 하나를 삭제합니다.",
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
async def delete_unique_test_table_row_sample(
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
    return await service.delete_unique_test_table_row_sample(
        request,
        response,
        index,
        delete_logically
    )


# ----
@router.post(
    "/fk-parent",
    response_model=model.PostFkParentRowSampleOutputVo,
    summary="외래키 부모 테이블 Row 입력 API",
    description="외래키 부모 테이블에 Row 를 입력합니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def post_fk_parent_row_sample(
        request: Request,
        response: Response,
        request_body: model.PostFkParentRowSampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.post_fk_parent_row_sample(request, response, request_body)


# ----
@router.post(
    "/fk-parent/{parentUid}",
    response_model=model.PostFkChildRowSampleOutputVo,
    summary="외래키 부모 테이블 아래에 자식 테이블의 Row 입력 API",
    description="외래키 부모 테이블의 아래에 자식 테이블의 Row 를 입력합니다.",
    responses={
        200: {"description": "OK"},
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : parentUid 에 해당하는 데이터가 존재하지 않습니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    }
)
async def post_fk_child_row_sample(
        request: Request,
        response: Response,
        parent_uid: int = Path(
            ...,
            alias="parentUid",
            description="외래키 부모 테이블 고유번호",
            example=1
        ),
        request_body: model.PostFkChildRowSampleInputVo =
        Body(
            ...,
            description="Body 파라미터"
        )
):
    return await service.post_fk_child_row_sample(request, response, parent_uid, request_body)


# ----
@router.get(
    "/fk-table/all",
    response_model=model.GetFkTestTableRowsSampleOutputVo,
    summary="외래키 관련 테이블 Rows 조회 테스트",
    description="외래키 관련 테이블의 모든 Rows 를 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def select_fk_test_table_rows_sample(
        request: Request,
        response: Response
):
    return await service.select_fk_test_table_rows_sample(
        request,
        response
    )


# ----
@router.get(
    "/fk-table-native-join",
    response_model=model.GetFkTestTableRowsByNativeQuerySampleDot1OutputVo,
    summary="외래키 관련 테이블 Rows 조회 테스트(Native Join)",
    description="외래키 관련 테이블의 모든 Rows 를 Native Query 로 Join 하여 반환합니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_fk_test_table_rows_by_native_query_sample(
        request: Request,
        response: Response
):
    return await service.get_fk_test_table_rows_by_native_query_sample(
        request,
        response
    )


# ----
@router.get(
    "/native-query-return",
    response_model=model.GetNativeQueryReturnValueTestOutputVo,
    summary="Native Query 반환값 테스트",
    description="Native Query Select 문에서 IF, CASE 등의 문구에서 반환되는 값들을 받는 예시",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def get_native_query_return_value_test(
        request: Request,
        response: Response,
        input_val: bool =
        Query(
            ...,
            alias="inputVal",
            description="Native Query 비교문에 사용되는 파라미터",
            example=True
        )
):
    return await service.get_native_query_return_value_test(
        request,
        response,
        input_val
    )


# ----
@router.get(
    "/fk-table-latest-join",
    response_model=model.SelectFkTableRowsWithLatestChildSampleOutputVo,
    summary="외래키 관련 테이블 Rows 조회 (네이티브 쿼리, 부모 테이블을 자식 테이블의 가장 최근 데이터만 Join)",
    description="외래키 관련 테이블의 모든 Rows 를 반환합니다.<br>"
                "부모 테이블을 Native Query 로 조회할 때, 부모 테이블을 가리키는 자식 테이블들 중 가장 최신 데이터만 Join 하는 예시입니다.",
    responses={
        200: {
            "description": "OK"
        }
    }
)
async def select_fk_table_rows_with_latest_child_sample(
        request: Request,
        response: Response
):
    return await service.select_fk_table_rows_with_latest_child_sample(
        request,
        response
    )


# ----
@router.delete(
    "/fk-child/{index}",
    summary="외래키 자식 테이블 Row 삭제 테스트",
    description="외래키 자식 테이블의 Row 하나를 삭제합니다.",
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
async def delete_fk_child_row_sample(
        request: Request,
        response: Response,
        index: int = Path(
            ...,
            alias="index",
            description="글 인덱스",
            example=1
        )
):
    return await service.delete_fk_child_row_sample(
        request,
        response,
        index
    )


# ----
@router.delete(
    "/fk-parent/{index}",
    summary="외래키 부모 테이블 Row 삭제 테스트 (Cascade 기능 확인)",
    description="외래키 부모 테이블의 Row 하나를 삭제합니다.<br>"
                "Cascade 설정을 했으므로 부모 테이블이 삭제되면 해당 부모 테이블을 참조중인 다른 모든 자식 테이블들이 삭제되어야 합니다.",
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
async def delete_fk_parent_row_sample(
        request: Request,
        response: Response,
        index: int = Path(
            ...,
            alias="index",
            description="글 인덱스",
            example=1
        )
):
    return await service.delete_fk_parent_row_sample(
        request,
        response,
        index
    )


# ----
@router.post(
    "/fk-transaction-rollback-sample",
    summary="외래키 테이블 트랜젝션 동작 테스트",
    description="외래키 테이블에 정보 입력 후 Exception 이 발생했을 때 롤백되어 데이터가 저장되지 않는지를 테스트하는 API",
    responses={
        200: {
            "description": "OK",
            "content": {"*/*": {}}
        }
    },
    response_class=Response
)
async def fk_table_transaction_test(
        request: Request,
        response: Response
):
    return await service.fk_table_transaction_test(request, response)
