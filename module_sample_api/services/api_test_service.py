import module_sample_api.models.api_test_model as model
import fastapi
import typing


# [그룹 서비스]
# (Get 요청 테스트 (Query Parameter))
def get_request_test(
        query_param_string: str,
        query_param_string_nullable: typing.Optional[str],
        query_param_int: int,
        query_param_int_nullable: typing.Optional[int],
        query_param_double: float,
        query_param_double_nullable: typing.Optional[float],
        query_param_boolean: bool,
        query_param_boolean_nullable: typing.Optional[bool],
        query_param_string_list: typing.List[str],
        query_param_string_list_nullable: typing.Optional[typing.List[str]]
):
    return fastapi.responses.JSONResponse(
        status_code=200,
        content=model.GetRequestTestOutputVo(
            query_param_string=query_param_string,
            query_param_string_nullable=query_param_string_nullable,
            query_param_int=query_param_int,
            query_param_int_nullable=query_param_int_nullable,
            query_param_double=query_param_double,
            query_param_double_nullable=query_param_double_nullable,
            query_param_boolean=query_param_boolean,
            query_param_boolean_nullable=query_param_boolean_nullable,
            query_param_string_list=query_param_string_list,
            query_param_string_list_nullable=query_param_string_list_nullable
        ).model_dump()
    )


# ----
# (Get 요청 테스트 (Path Parameter))
def get_request_test_with_path_param(
        path_param_int: int
):
    return fastapi.responses.JSONResponse(
        status_code=200,
        content=model.GetRequestTestWithPathParamOutputVo(
            path_param_int=path_param_int
        ).model_dump()
    )


# ----
# (Post 요청 테스트 (application-json))
def post_request_test_with_application_json_type_request_body(
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBodyInputVo
):
    return fastapi.responses.JSONResponse(
        status_code=200,
        content=model.PostRequestTestWithApplicationJsonTypeRequestBodyOutputVo(
            request_body_string=request_body.request_body_string,
            request_body_string_nullable=request_body.request_body_string_nullable,
            request_body_int=request_body.request_body_int,
            request_body_int_nullable=request_body.request_body_int_nullable,
            request_body_double=request_body.request_body_double,
            request_body_double_nullable=request_body.request_body_double_nullable,
            request_body_boolean=request_body.request_body_boolean,
            request_body_boolean_nullable=request_body.request_body_boolean_nullable,
            request_body_string_list=request_body.request_body_string_list,
            request_body_string_list_nullable=request_body.request_body_string_list_nullable
        ).model_dump()
    )
