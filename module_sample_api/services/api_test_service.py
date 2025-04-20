import module_sample_api.controllers.api_test_controller as controller
import fastapi
import typing


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
        content=controller.GetRequestTestOutputVo(
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
        ).model_dump()
    )


# ----
# (Get 요청 테스트 (Path Parameter))
def get_request_test_with_path_param(path_param_int):
    return fastapi.responses.JSONResponse(
        status_code=200,
        content=controller.GetRequestTestWithPathParamOutputVo(
            pathParamInt=path_param_int
        ).model_dump()
    )

# ----
