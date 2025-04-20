import typing
import pydantic


# [그룹 모델]
# (Get 요청 테스트 (Query Parameter))
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

    class Config:
        validate_by_name = True


# ----
# (Get 요청 테스트 (Path Parameter))
class GetRequestTestWithPathParamOutputVo(pydantic.BaseModel):
    path_param_int: int = pydantic.Field(
        ...,
        alias="pathParamInt",
        description="입력한 Int Path 파라미터",
        examples=[1]
    )

    class Config:
        validate_by_name = True


# ----
# (Post 요청 테스트 (application-json))
class PostRequestTestWithApplicationJsonTypeRequestBodyInputVo(pydantic.BaseModel):
    request_body_string: str = (
        pydantic.Field(
            ...,
            alias="requestBodyString",
            description="String Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_string_nullable: typing.Optional[str] = (
        pydantic.Field(
            None,
            alias="requestBodyStringNullable",
            description="String Nullable Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_int: int = (
        pydantic.Field(
            ...,
            alias="requestBodyInt",
            description="Int Body 파라미터",
            examples=[1]
        )
    )
    request_body_int_nullable: typing.Optional[int] = (
        pydantic.Field(
            None,
            alias="requestBodyIntNullable",
            description="Int Nullable Body 파라미터",
            examples=[1]
        )
    )
    request_body_double: float = (
        pydantic.Field(
            ...,
            alias="requestBodyDouble",
            description="Double Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_double_nullable: typing.Optional[float] = (
        pydantic.Field(
            None,
            alias="requestBodyDoubleNullable",
            description="Double Nullable Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_boolean: bool = (
        pydantic.Field(
            ...,
            alias="requestBodyBoolean",
            description="Boolean Body 파라미터",
            examples=[True]
        )
    )
    request_body_boolean_nullable: typing.Optional[bool] = (
        pydantic.Field(
            None,
            alias="requestBodyBooleanNullable",
            description="Boolean Nullable Body 파라미터",
            examples=[True]
        )
    )
    request_body_string_list: typing.List[str] = (
        pydantic.Field(
            ...,
            alias="requestBodyStringList",
            description="StringList Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    request_body_string_list_nullable: typing.Optional[typing.List[str]] = (
        pydantic.Field(
            None,
            alias="requestBodyStringListNullable",
            description="StringList Nullable Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )

    class Config:
        validate_by_name = True


class PostRequestTestWithApplicationJsonTypeRequestBodyOutputVo(pydantic.BaseModel):
    request_body_string: str = (
        pydantic.Field(
            ...,
            alias="requestBodyString",
            description="입력한 String Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_string_nullable: typing.Optional[str] = (
        pydantic.Field(
            None,
            alias="requestBodyStringNullable",
            description="입력한 String Nullable Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_int: int = (
        pydantic.Field(
            ...,
            alias="requestBodyInt",
            description="입력한 Int Body 파라미터",
            examples=[1]
        )
    )
    request_body_int_nullable: typing.Optional[int] = (
        pydantic.Field(
            None,
            alias="requestBodyIntNullable",
            description="입력한 Int Nullable Body 파라미터",
            examples=[1]
        )
    )
    request_body_double: float = (
        pydantic.Field(
            ...,
            alias="requestBodyDouble",
            description="입력한 Double Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_double_nullable: typing.Optional[float] = (
        pydantic.Field(
            None,
            alias="requestBodyDoubleNullable",
            description="입력한 Double Nullable Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_boolean: bool = (
        pydantic.Field(
            ...,
            alias="requestBodyBoolean",
            description="입력한 Boolean Body 파라미터",
            examples=[True]
        )
    )
    request_body_boolean_nullable: typing.Optional[bool] = (
        pydantic.Field(
            None,
            alias="requestBodyBooleanNullable",
            description="입력한 Boolean Nullable Body 파라미터",
            examples=[True]
        )
    )
    request_body_string_list: typing.List[str] = (
        pydantic.Field(
            ...,
            alias="requestBodyStringList",
            description="입력한 StringList Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    request_body_string_list_nullable: typing.Optional[typing.List[str]] = (
        pydantic.Field(
            None,
            alias="requestBodyStringListNullable",
            description="입력한 StringList Nullable Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )

    class Config:
        validate_by_name = True
