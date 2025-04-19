import fastapi
import typing
import pydantic
import module_sample_api.services.api_test_service as service

# Router 설정
router = fastapi.APIRouter(
    prefix="/user",  # 전체 경로 앞에 붙는 prefix
    tags=["User API"]  # Swagger 문서 그룹 이름
)


# ----------------------------------------------------------------------------------------------------------------------
# <API 선언 공간>
class GetRequestTestOutputVo(pydantic.BaseModel):
    query_param_string: str = (
        pydantic.Field(
            ...,
            alias="queryParamString",
            description="입력한 String Query 파라미터",
            examples=["testString"]
        )
    )
    query_param_string_nullable: typing.Optional[str] = (
        pydantic.Field(
            None,
            alias="queryParamStringNullable",
            description="입력한 String Nullable Query 파라미터",
            examples=["testString"]
        )
    )
    query_param_int: int = (
        pydantic.Field(
            ...,
            alias="queryParamInt",
            description="입력한 Int Query 파라미터",
            examples=[1]
        )
    )
    query_param_int_nullable: typing.Optional[int] = (
        pydantic.Field(
            None,
            alias="queryParamIntNullable",
            description="입력한 Int Nullable Query 파라미터",
            examples=[1]
        )
    )
    query_param_double: float = (
        pydantic.Field(
            ...,
            alias="queryParamDouble",
            description="입력한 Double Query 파라미터",
            examples=[1.1]
        )
    )
    query_param_double_nullable: typing.Optional[float] = (
        pydantic.Field(
            None,
            alias="queryParamDoubleNullable",
            description="입력한 Double Nullable Query 파라미터",
            examples=[1.1]
        )
    )
    query_param_boolean: bool = (
        pydantic.Field(
            ...,
            alias="queryParamBoolean",
            description="입력한 Boolean Query 파라미터",
            examples=[True]
        )
    )
    query_param_boolean_nullable: typing.Optional[bool] = (
        pydantic.Field(
            None,
            alias="queryParamBooleanNullable",
            description="입력한 Boolean Nullable Query 파라미터",
            examples=[True]
        )
    )
    query_param_string_list: typing.List[str] = (
        pydantic.Field(
            ...,
            alias="queryParamStringList",
            description="입력한 StringList Query 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    query_param_string_list_nullable: typing.Optional[typing.List[str]] = (
        pydantic.Field(
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
        fastapi.Query(
            ...,
            alias="queryParamString",
            description="String Query 파라미터",
            example="testString"
        ),
        query_param_string_nullable: typing.Optional[str] =
        fastapi.Query(
            None,
            alias="queryParamStringNullable",
            description="String Query 파라미터 Nullable",
            example="testString"
        ),
        query_param_int: int =
        fastapi.Query(
            ...,
            alias="queryParamInt",
            description="Int Query 파라미터",
            example=1
        ),
        query_param_int_nullable: typing.Optional[int] =
        fastapi.Query(
            None,
            alias="queryParamIntNullable",
            description="Int Query 파라미터 Nullable",
            example=1
        ),
        query_param_double: float =
        fastapi.Query(
            ...,
            alias="queryParamDouble",
            description="Double Query 파라미터",
            example=1.1
        ),
        query_param_double_nullable: typing.Optional[float] =
        fastapi.Query(
            None,
            alias="queryParamDoubleNullable",
            description="Double Query 파라미터 Nullable",
            example=1.1
        ),
        query_param_boolean: bool =
        fastapi.Query(
            ...,
            alias="queryParamBoolean",
            description="Boolean Query 파라미터",
            example=True
        ),
        query_param_boolean_nullable: typing.Optional[bool] =
        fastapi.Query(
            None,
            alias="queryParamBooleanNullable",
            description="Boolean Query 파라미터 Nullable",
            example=True
        ),
        query_param_string_list: typing.List[str] =
        fastapi.Query(
            ...,
            alias="queryParamStringList",
            description="StringList Query 파라미터",
            example=["testString1", "testString2"]
        ),
        query_param_string_list_nullable: typing.Optional[typing.List[str]] =
        fastapi.Query(
            None,
            alias="queryParamStringListNullable",
            description="StringList Query 파라미터 Nullable",
            example=["testString1", "testString2"]
        )
):
    return service.get_request_test(
        query_param_string,
        query_param_string_nullable,
        query_param_int,
        query_param_int_nullable,
        query_param_double,
        query_param_double_nullable,
        query_param_boolean,
        query_param_boolean_nullable,
        query_param_string_list,
        query_param_string_list_nullable
    )

# ----
