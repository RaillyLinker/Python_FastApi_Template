import os
from fastapi import responses, UploadFile
from typing import Optional, List
from fastapi.responses import RedirectResponse
from module_sample_api.configurations.app_conf import AppConf
import module_sample_api.utils.custom_util as custom_util
import module_sample_api.models.api_test_model as model


# [그룹 서비스]
# (기본 요청 테스트 API)
async def basic_request_test():
    return AppConf.server_profile


# ----
# (요청 Redirect 테스트 API)
async def redirect_test():
    return RedirectResponse(url="/api-test")


# ----
# (Get 요청 테스트 (Query Parameter))
async def get_request_test(
        query_param_string: str,
        query_param_string_nullable: Optional[str],
        query_param_int: int,
        query_param_int_nullable: Optional[int],
        query_param_double: float,
        query_param_double_nullable: Optional[float],
        query_param_boolean: bool,
        query_param_boolean_nullable: Optional[bool],
        query_param_string_list: List[str],
        query_param_string_list_nullable: Optional[List[str]]
):
    return responses.JSONResponse(
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
async def get_request_test_with_path_param(
        path_param_int: int
):
    return responses.JSONResponse(
        status_code=200,
        content=model.GetRequestTestWithPathParamOutputVo(
            path_param_int=path_param_int
        ).model_dump()
    )


# ----
# (Post 요청 테스트 (application-json))
async def post_request_test_with_application_json_type_request_body(
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBodyInputVo
):
    return responses.JSONResponse(
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


# ----
# (Post 요청 테스트 (application-json, 객체 파라미터 포함))
async def post_request_test_with_application_json_type_request_body2(
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBody2InputVo
):
    # objectVoList 변환
    object_vo_list: List[model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput] = []
    for object_vo in request_body.object_vo_list:
        sub_object_vo_list: List[
            model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput.SubObjectVoOutput] = [
            model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput.SubObjectVoOutput(
                request_body_string=sub.request_body_string,
                request_body_string_list=sub.request_body_string_list
            ) for sub in object_vo.sub_object_vo_list
        ]

        object_vo_output = model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput(
            request_body_string=object_vo.request_body_string,
            request_body_string_list=object_vo.request_body_string_list,
            sub_object_vo=
            model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput.SubObjectVoOutput(
                request_body_string=object_vo.sub_object_vo.request_body_string,
                request_body_string_list=object_vo.sub_object_vo.request_body_string_list
            ),
            sub_object_vo_list=sub_object_vo_list
        )
        object_vo_list.append(object_vo_output)

    # objectVo 단일 항목 변환
    sub_object_vo_list_single: List[
        model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput.SubObjectVoOutput] = [
        model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput.SubObjectVoOutput(
            request_body_string=sub.request_body_string,
            request_body_string_list=sub.request_body_string_list
        ) for sub in request_body.object_vo.sub_object_vo_list
    ]

    object_vo_single = model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput(
        request_body_string=request_body.object_vo.request_body_string,
        request_body_string_list=request_body.object_vo.request_body_string_list,
        sub_object_vo=model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo.ObjectVoOutput.SubObjectVoOutput(
            request_body_string=request_body.object_vo.sub_object_vo.request_body_string,
            request_body_string_list=request_body.object_vo.sub_object_vo.request_body_string_list
        ),
        sub_object_vo_list=sub_object_vo_list_single
    )

    return responses.JSONResponse(
        status_code=200,
        content=model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo(
            object_vo=object_vo_single,
            object_vo_list=object_vo_list
        ).model_dump()
    )


# ----
# (Post 요청 테스트 (입출력값 없음))
async def post_request_test_with_no_input_and_output():
    return responses.JSONResponse(
        status_code=200,
        content=None
    )


# ----
# (Post 요청 테스트 (x-www-form-urlencoded))
async def post_request_test_with_form_type_request_body(
        request_form_string: str,
        request_form_string_nullable: Optional[str],
        request_form_int: int,
        request_form_int_nullable: Optional[int],
        request_form_double: float,
        request_form_double_nullable: Optional[float],
        request_form_boolean: bool,
        request_form_boolean_nullable: Optional[bool],
        request_form_string_list: List[str],
        request_form_string_list_nullable: Optional[List[str]]
):
    return responses.JSONResponse(
        status_code=200,
        content=model.PostRequestTestWithFormTypeRequestBodyOutputVo(
            request_form_string=request_form_string,
            request_form_string_nullable=request_form_string_nullable,
            request_form_int=request_form_int,
            request_form_int_nullable=request_form_int_nullable,
            request_form_double=request_form_double,
            request_form_double_nullable=request_form_double_nullable,
            request_form_boolean=request_form_boolean,
            request_form_boolean_nullable=request_form_boolean_nullable,
            request_form_string_list=request_form_string_list,
            request_form_string_list_nullable=request_form_string_list_nullable
        ).model_dump()
    )


# ----
# (Post 요청 테스트 (x-www-form-urlencoded))
async def post_request_test_with_multipart_form_type_request_body(
        request_form_string: str,
        request_form_string_nullable: Optional[str],
        request_form_int: int,
        request_form_int_nullable: Optional[int],
        request_form_double: float,
        request_form_double_nullable: Optional[float],
        request_form_boolean: bool,
        request_form_boolean_nullable: Optional[bool],
        request_form_string_list: List[str],
        request_form_string_list_nullable: Optional[List[str]],
        multipart_file: UploadFile,
        multipart_file_nullable: Optional[UploadFile]
):
    # 저장 경로 설정
    save_directory_path = os.path.abspath("./by_product_files/sample_api/test")

    # 파일 저장 (필수)
    custom_util.multipart_file_local_save(save_directory_path, None, multipart_file)

    # 파일 저장 (nullable)
    if multipart_file_nullable is not None:
        custom_util.multipart_file_local_save(save_directory_path, None, multipart_file_nullable)

    return responses.JSONResponse(
        status_code=200,
        content=model.PostRequestTestWithMultipartFormTypeRequestBodyOutputVo(
            request_form_string=request_form_string,
            request_form_string_nullable=request_form_string_nullable,
            request_form_int=request_form_int,
            request_form_int_nullable=request_form_int_nullable,
            request_form_double=request_form_double,
            request_form_double_nullable=request_form_double_nullable,
            request_form_boolean=request_form_boolean,
            request_form_boolean_nullable=request_form_boolean_nullable,
            request_form_string_list=request_form_string_list,
            request_form_string_list_nullable=request_form_string_list_nullable
        ).model_dump()
    )
