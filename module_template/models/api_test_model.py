from typing import Optional, List
from pydantic import BaseModel, Field


# [그룹 모델]
# (Get 요청 테스트 (Query Parameter))
class GetRequestTestOutputVo(BaseModel):
    class Config:
        validate_by_name = True

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


# ----
# (Get 요청 테스트 (Path Parameter))
class GetRequestTestWithPathParamOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    path_param_int: int = Field(
        ...,
        alias="pathParamInt",
        description="입력한 Int Path 파라미터",
        examples=[1]
    )


# ----
# (Post 요청 테스트 (application-json))
class PostRequestTestWithApplicationJsonTypeRequestBodyInputVo(BaseModel):
    class Config:
        validate_by_name = True

    request_body_string: str = (
        Field(
            ...,
            alias="requestBodyString",
            description="String Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_string_nullable: Optional[str] = (
        Field(
            None,
            alias="requestBodyStringNullable",
            description="String Nullable Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_int: int = (
        Field(
            ...,
            alias="requestBodyInt",
            description="Int Body 파라미터",
            examples=[1]
        )
    )
    request_body_int_nullable: Optional[int] = (
        Field(
            None,
            alias="requestBodyIntNullable",
            description="Int Nullable Body 파라미터",
            examples=[1]
        )
    )
    request_body_double: float = (
        Field(
            ...,
            alias="requestBodyDouble",
            description="Double Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_double_nullable: Optional[float] = (
        Field(
            None,
            alias="requestBodyDoubleNullable",
            description="Double Nullable Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_boolean: bool = (
        Field(
            ...,
            alias="requestBodyBoolean",
            description="Boolean Body 파라미터",
            examples=[True]
        )
    )
    request_body_boolean_nullable: Optional[bool] = (
        Field(
            None,
            alias="requestBodyBooleanNullable",
            description="Boolean Nullable Body 파라미터",
            examples=[True]
        )
    )
    request_body_string_list: List[str] = (
        Field(
            ...,
            alias="requestBodyStringList",
            description="StringList Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    request_body_string_list_nullable: Optional[List[str]] = (
        Field(
            None,
            alias="requestBodyStringListNullable",
            description="StringList Nullable Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )


class PostRequestTestWithApplicationJsonTypeRequestBodyOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    request_body_string: str = (
        Field(
            ...,
            alias="requestBodyString",
            description="입력한 String Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_string_nullable: Optional[str] = (
        Field(
            None,
            alias="requestBodyStringNullable",
            description="입력한 String Nullable Body 파라미터",
            examples=["testString"]
        )
    )
    request_body_int: int = (
        Field(
            ...,
            alias="requestBodyInt",
            description="입력한 Int Body 파라미터",
            examples=[1]
        )
    )
    request_body_int_nullable: Optional[int] = (
        Field(
            None,
            alias="requestBodyIntNullable",
            description="입력한 Int Nullable Body 파라미터",
            examples=[1]
        )
    )
    request_body_double: float = (
        Field(
            ...,
            alias="requestBodyDouble",
            description="입력한 Double Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_double_nullable: Optional[float] = (
        Field(
            None,
            alias="requestBodyDoubleNullable",
            description="입력한 Double Nullable Body 파라미터",
            examples=[1.1]
        )
    )
    request_body_boolean: bool = (
        Field(
            ...,
            alias="requestBodyBoolean",
            description="입력한 Boolean Body 파라미터",
            examples=[True]
        )
    )
    request_body_boolean_nullable: Optional[bool] = (
        Field(
            None,
            alias="requestBodyBooleanNullable",
            description="입력한 Boolean Nullable Body 파라미터",
            examples=[True]
        )
    )
    request_body_string_list: List[str] = (
        Field(
            ...,
            alias="requestBodyStringList",
            description="입력한 StringList Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    request_body_string_list_nullable: Optional[List[str]] = (
        Field(
            None,
            alias="requestBodyStringListNullable",
            description="입력한 StringList Nullable Body 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )


# ----
# (Post 요청 테스트 (application-json, 객체 파라미터 포함))
class PostRequestTestWithApplicationJsonTypeRequestBody2InputVo(BaseModel):
    class Config:
        validate_by_name = True

    class ObjectVoInput(BaseModel):
        class Config:
            validate_by_name = True

        class SubObjectVoInput(BaseModel):
            class Config:
                validate_by_name = True

            request_body_string: str = (
                Field(
                    ...,
                    alias="requestBodyString",
                    description="String Body 파라미터",
                    examples=["testString"]
                )
            )
            request_body_string_list: List[str] = (
                Field(
                    ...,
                    alias="requestBodyStringList",
                    description="StringList Body 파라미터",
                    examples=[["testString1", "testString2"]]
                )
            )

        request_body_string: str = (
            Field(
                ...,
                alias="requestBodyString",
                description="String Body 파라미터",
                examples=["testString"]
            )
        )

        request_body_string_list: List[str] = (
            Field(
                ...,
                alias="requestBodyStringList",
                description="StringList Body 파라미터",
                examples=[["testString1", "testString2"]]
            )
        )

        sub_object_vo: SubObjectVoInput = (
            Field(
                ...,
                alias="subObjectVo",
                description="서브 객체 타입 파라미터"
            )
        )
        sub_object_vo_list: List[SubObjectVoInput] = (
            Field(
                ...,
                alias="subObjectVoList",
                description="서브 객체 타입 리스트 파라미터"
            )
        )

    object_vo: ObjectVoInput = (
        Field(
            ...,
            alias="objectVo",
            description="객체 타입 파라미터"
        )
    )
    object_vo_list: List[ObjectVoInput] = (
        Field(
            ...,
            alias="objectVoList",
            description="객체 타입 리스트 파라미터"
        )
    )


class PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class ObjectVoOutput(BaseModel):
        class Config:
            validate_by_name = True

        class SubObjectVoOutput(BaseModel):
            class Config:
                validate_by_name = True

            request_body_string: str = (
                Field(
                    ...,
                    alias="requestBodyString",
                    description="String Body 파라미터",
                    examples=["testString"]
                )
            )
            request_body_string_list: List[str] = (
                Field(
                    ...,
                    alias="requestBodyStringList",
                    description="StringList Body 파라미터",
                    examples=[["testString1", "testString2"]]
                )
            )

        request_body_string: str = (
            Field(
                ...,
                alias="requestBodyString",
                description="String Body 파라미터",
                examples=["testString"]
            )
        )
        request_body_string_list: List[str] = (
            Field(
                ...,
                alias="requestBodyStringList",
                description="StringList Body 파라미터",
                examples=[["testString1", "testString2"]]
            )
        )

        sub_object_vo: SubObjectVoOutput = (
            Field(
                ...,
                alias="subObjectVo",
                description="서브 객체 타입 파라미터"
            )
        )
        sub_object_vo_list: List[SubObjectVoOutput] = (
            Field(
                ...,
                alias="subObjectVoList",
                description="서브 객체 타입 리스트 파라미터"
            )
        )

    object_vo: ObjectVoOutput = (
        Field(
            ...,
            alias="objectVo",
            description="객체 타입 파라미터"
        )
    )
    object_vo_list: List[ObjectVoOutput] = (
        Field(
            ...,
            alias="objectVoList",
            description="객체 타입 리스트 파라미터"
        )
    )


# ----
# (Post 요청 테스트 (x-www-form-urlencoded))
class PostRequestTestWithFormTypeRequestBodyOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    request_form_string: str = (
        Field(
            ...,
            alias="requestFormString",
            description="입력한 String Form 파라미터",
            examples=["testString"]
        )
    )
    request_form_string_nullable: Optional[str] = (
        Field(
            None,
            alias="requestFormStringNullable",
            description="입력한 String Nullable Form 파라미터",
            examples=["testString"]
        )
    )
    request_form_int: int = (
        Field(
            ...,
            alias="requestFormInt",
            description="입력한 Int Form 파라미터",
            examples=[1]
        )
    )
    request_form_int_nullable: Optional[int] = (
        Field(
            None,
            alias="requestFormIntNullable",
            description="입력한 Int Nullable Form 파라미터",
            examples=[1]
        )
    )
    request_form_double: float = (
        Field(
            ...,
            alias="requestFormDouble",
            description="입력한 Double Form 파라미터",
            examples=[1.1]
        )
    )
    request_form_double_nullable: Optional[float] = (
        Field(
            None,
            alias="requestFormDoubleNullable",
            description="입력한 Double Nullable Form 파라미터",
            examples=[1.1]
        )
    )
    request_form_boolean: bool = (
        Field(
            ...,
            alias="requestFormBoolean",
            description="입력한 Boolean Form 파라미터",
            examples=[True]
        )
    )
    request_form_boolean_nullable: Optional[bool] = (
        Field(
            None,
            alias="requestFormBooleanNullable",
            description="입력한 Boolean Nullable Form 파라미터",
            examples=[True]
        )
    )
    request_form_string_list: List[str] = (
        Field(
            ...,
            alias="requestFormStringList",
            description="입력한 StringList Form 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    request_form_string_list_nullable: Optional[List[str]] = (
        Field(
            None,
            alias="requestFormStringListNullable",
            description="입력한 StringList Nullable Form 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )


# ----
# (Post 요청 테스트 (multipart/form-data))
class PostRequestTestWithMultipartFormTypeRequestBodyOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    request_form_string: str = (
        Field(
            ...,
            alias="requestFormString",
            description="입력한 String Form 파라미터",
            examples=["testString"]
        )
    )
    request_form_string_nullable: Optional[str] = (
        Field(
            None,
            alias="requestFormStringNullable",
            description="입력한 String Nullable Form 파라미터",
            examples=["testString"]
        )
    )
    request_form_int: int = (
        Field(
            ...,
            alias="requestFormInt",
            description="입력한 Int Form 파라미터",
            examples=[1]
        )
    )
    request_form_int_nullable: Optional[int] = (
        Field(
            None,
            alias="requestFormIntNullable",
            description="입력한 Int Nullable Form 파라미터",
            examples=[1]
        )
    )
    request_form_double: float = (
        Field(
            ...,
            alias="requestFormDouble",
            description="입력한 Double Form 파라미터",
            examples=[1.1]
        )
    )
    request_form_double_nullable: Optional[float] = (
        Field(
            None,
            alias="requestFormDoubleNullable",
            description="입력한 Double Nullable Form 파라미터",
            examples=[1.1]
        )
    )
    request_form_boolean: bool = (
        Field(
            ...,
            alias="requestFormBoolean",
            description="입력한 Boolean Form 파라미터",
            examples=[True]
        )
    )
    request_form_boolean_nullable: Optional[bool] = (
        Field(
            None,
            alias="requestFormBooleanNullable",
            description="입력한 Boolean Nullable Form 파라미터",
            examples=[True]
        )
    )
    request_form_string_list: List[str] = (
        Field(
            ...,
            alias="requestFormStringList",
            description="입력한 StringList Form 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
    request_form_string_list_nullable: Optional[List[str]] = (
        Field(
            None,
            alias="requestFormStringListNullable",
            description="입력한 StringList Nullable Form 파라미터",
            examples=[["testString1", "testString2"]]
        )
    )
