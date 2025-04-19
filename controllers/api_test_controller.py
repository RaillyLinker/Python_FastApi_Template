from fastapi import APIRouter
from fastapi import Query
from typing import Optional, List
from pydantic import BaseModel, Field

# Router 설정
router = APIRouter(
    prefix="/user",  # 전체 경로 앞에 붙는 prefix
    tags=["User API"]  # Swagger 문서 그룹 이름
)


# ----------------------------------------------------------------------------------------------------------------------
# <API 선언 공간>
class GetRequestTestOutputVo(BaseModel):
    query_param_string: str = (
        Field(
            ...,
            alias="queryParamString",
            description="입력한 String Query 파라미터",
            examples=["testString"]
        )
    )
    query_param_string_nullable: Optional[str] = (
        Field(
            None,
            alias="queryParamStringNullable",
            description="입력한 String Nullable Query 파라미터",
            examples=["testString"]
        )
    )
    query_param_int: int = (
        Field(
            ...,
            alias="queryParamInt",
            description="입력한 Int Query 파라미터",
            examples=[1]
        )
    )
    query_param_int_nullable: Optional[int] = (
        Field(
            None,
            alias="queryParamIntNullable",
            description="입력한 Int Nullable Query 파라미터",
            examples=[1]
        )
    )
    query_param_double: float = (
        Field(
            ...,
            alias="queryParamDouble",
            description="입력한 Double Query 파라미터",
            examples=[1.1]
        )
    )
    query_param_double_nullable: Optional[float] = (
        Field(
            None,
            alias="queryParamDoubleNullable",
            description="입력한 Double Nullable Query 파라미터",
            examples=[1.1]
        )
    )
    query_param_boolean: bool = (
        Field(
            ...,
            alias="queryParamBoolean",
            description="입력한 Boolean Query 파라미터",
            examples=[True]
        )
    )
    query_param_boolean_nullable: Optional[bool] = (
        Field(
            None,
            alias="queryParamBooleanNullable",
            description="입력한 Boolean Nullable Query 파라미터",
            examples=[True]
        )
    )
    query_param_string_list: List[str] = (
        Field(
            ...,
            alias="queryParamStringList",
            description="입력한 StringList Query 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    query_param_string_list_nullable: Optional[List[str]] = (
        Field(
            None,
            alias="queryParamStringListNullable",
            description="입력한 StringList Nullable Query 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )


@router.get(
    "/get-request",
    response_model=GetRequestTestOutputVo,
    summary="Get 요청 테스트 (Query Parameter)",
    description="Query Parameter 를 받는 Get 메소드 요청 테스트"
)
def get_request_test(
        query_param_string: str =
        Query(
            ...,
            alias="queryParamString",
            description="String Query 파라미터",
            example="testString"
        ),
        query_param_string_nullable: Optional[str] =
        Query(
            None,
            alias="queryParamStringNullable",
            description="String Query 파라미터 Nullable",
            example="testString"
        ),
        query_param_int: int =
        Query(
            ...,
            alias="queryParamInt",
            description="Int Query 파라미터",
            example=1
        ),
        query_param_int_nullable: Optional[int] =
        Query(
            None,
            alias="queryParamIntNullable",
            description="Int Query 파라미터 Nullable",
            example=1
        ),
        query_param_double: float =
        Query(
            ...,
            alias="queryParamDouble",
            description="Double Query 파라미터",
            example=1.1
        ),
        query_param_double_nullable: Optional[float] =
        Query(
            None,
            alias="queryParamDoubleNullable",
            description="Double Query 파라미터 Nullable",
            example=1.1
        ),
        query_param_boolean: bool =
        Query(
            ...,
            alias="queryParamBoolean",
            description="Boolean Query 파라미터",
            example=True
        ),
        query_param_boolean_nullable: Optional[bool] =
        Query(
            None,
            alias="queryParamBooleanNullable",
            description="Boolean Query 파라미터 Nullable",
            example=True
        ),
        query_param_string_list: List[str] =
        Query(
            ...,
            alias="queryParamStringList",
            description="StringList Query 파라미터",
            example=["testString1", "testString2"]
        ),
        query_param_string_list_nullable: Optional[List[str]] =
        Query(
            None,
            alias="queryParamStringListNullable",
            description="StringList Query 파라미터 Nullable",
            example=["testString1", "testString2"]
        )
):
    return GetRequestTestOutputVo(
        queryParamString=query_param_string,
        queryParamStringNullable=query_param_string_nullable,
        queryParamInt=query_param_int,
        queryParamIntNullable=query_param_int_nullable,
        queryParamDouble=query_param_double,
        queryParamDoubleNullable=query_param_double_nullable,
        queryParamBoolean=query_param_boolean,
        queryParamBooleanNullable=query_param_boolean_nullable,
        queryParamStringList=query_param_string_list,
        queryParamStringListNullable=query_param_string_list_nullable
    )

# ----
