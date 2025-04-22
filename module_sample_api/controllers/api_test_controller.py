import fastapi
import typing
import module_sample_api.services.api_test_service as service
import module_sample_api.models.api_test_model as model

# [그룹 컨트롤러]
# Router 설정
router = fastapi.APIRouter(
    prefix="/api-test",  # 전체 경로 앞에 붙는 prefix
    tags=["API 요청 / 응답에 대한 테스트 컨트롤러"]  # Swagger 문서 그룹 이름
)


# ----------------------------------------------------------------------------------------------------------------------
# <API 선언 공간>
@router.get(
    "/get-request",
    response_model=model.GetRequestTestOutputVo,
    summary="Get 요청 테스트 (Query Parameter)",
    description="Query Parameter 를 받는 Get 메소드 요청 테스트"
)
async def get_request_test(
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
    return await service.get_request_test(
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
@router.get(
    "/get-request/{pathParamInt}",
    response_model=model.GetRequestTestWithPathParamOutputVo,
    summary="Get 요청 테스트 (Path Parameter)",
    description="Path Parameter 를 받는 Get 메소드 요청 테스트",
)
async def get_request_test_with_path_param(
        path_param_int: int = fastapi.Path(
            ...,
            alias="pathParamInt",
            description="Int Path 파라미터",
            example=1
        )
):
    return await service.get_request_test_with_path_param(path_param_int)


# ----
@router.post(
    "/post-request-application-json",
    response_model=model.PostRequestTestWithApplicationJsonTypeRequestBodyOutputVo,
    summary="Post 요청 테스트 (application-json)",
    description="application-json 형태의 Request Body 를 받는 Post 메소드 요청 테스트"
)
async def post_request_test_with_application_json_type_request_body(
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBodyInputVo
):
    return await service.post_request_test_with_application_json_type_request_body(request_body)


# ----
@router.post(
    "/post-request-application-json-with-object-param",
    response_model=model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo,
    summary="Post 요청 테스트 (application-json, 객체 파라미터 포함)",
    description="application-json 형태의 Request Body(객체 파라미터 포함) 를 받는 Post 메소드 요청 테스트"
)
async def post_request_test_with_application_json_type_request_body2(
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBody2InputVo
):
    return await service.post_request_test_with_application_json_type_request_body2(request_body)


# ----
@router.post(
    "/post-request-application-json-with-no-param",
    response_class=fastapi.responses.PlainTextResponse,
    summary="Post 요청 테스트 (입출력값 없음)",
    description="입출력값이 없는 Post 메소드 요청 테스트"
)
async def post_request_test_with_no_input_and_output():
    return await service.post_request_test_with_no_input_and_output()


# ----
@router.post(
    "/post-request-x-www-form-urlencoded",
    response_model=model.PostRequestTestWithFormTypeRequestBodyOutputVo,
    summary="Post 요청 테스트 (x-www-form-urlencoded)",
    description="x-www-form-urlencoded 형태의 Request Body 를 받는 Post 메소드 요청 테스트"
)
async def post_request_test_with_form_type_request_body(
        request_form_string: str =
        fastapi.Form(
            ...,
            alias="requestFormString",
            validation_alias="requestFormString",
            description="String Form 파라미터",
            example="testString"
        ),
        request_form_string_nullable: typing.Optional[str] =
        fastapi.Form(
            None,
            alias="requestFormStringNullable",
            validation_alias="requestFormStringNullable",
            description="String Nullable Form 파라미터",
            example="testString"
        ),
        request_form_int: int =
        fastapi.Form(
            ...,
            alias="requestFormInt",
            validation_alias="requestFormInt",
            description="Int Form 파라미터",
            example=1
        ),
        request_form_int_nullable: typing.Optional[int] =
        fastapi.Form(
            None,
            alias="requestFormIntNullable",
            validation_alias="requestFormIntNullable",
            description="Int Nullable Form 파라미터",
            example=1
        ),
        request_form_double: float =
        fastapi.Form(
            ...,
            alias="requestFormDouble",
            validation_alias="requestFormDouble",
            description="Double Form 파라미터",
            example=1.1
        ),
        request_form_double_nullable: typing.Optional[float] =
        fastapi.Form(
            None,
            alias="requestFormDoubleNullable",
            validation_alias="requestFormDoubleNullable",
            description="Double Nullable Form 파라미터",
            example=1.1
        ),
        request_form_boolean: bool =
        fastapi.Form(
            ...,
            alias="requestFormBoolean",
            validation_alias="requestFormBoolean",
            description="Boolean Form 파라미터",
            example=True
        ),
        request_form_boolean_nullable: typing.Optional[bool] =
        fastapi.Form(
            None,
            alias="requestFormBooleanNullable",
            validation_alias="requestFormBooleanNullable",
            description="Boolean Nullable Form 파라미터",
            example=True
        ),
        request_form_string_list: typing.List[str] =
        fastapi.Form(
            ...,
            alias="requestFormStringList",
            validation_alias="requestFormStringList",
            description="StringList Form 파라미터",
            example=["testString1", "testString2"]
        ),
        request_form_string_list_nullable: typing.Optional[typing.List[str]] =
        fastapi.Form(
            None,
            alias="requestFormStringListNullable",
            validation_alias="requestFormStringListNullable",
            description="StringList Nullable Form 파라미터",
            example=["testString1", "testString2"]
        )
):
    return await service.post_request_test_with_form_type_request_body(
        request_form_string,
        request_form_string_nullable,
        request_form_int,
        request_form_int_nullable,
        request_form_double,
        request_form_double_nullable,
        request_form_boolean,
        request_form_boolean_nullable,
        request_form_string_list,
        request_form_string_list_nullable
    )
