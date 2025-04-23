import os
from fastapi import UploadFile, status, Response, Request, HTTPException
from fastapi.responses import PlainTextResponse, StreamingResponse
from typing import Optional, List
from fastapi.responses import RedirectResponse
from module_sample_api.configurations.app_conf import AppConf
import module_sample_api.utils.custom_util as custom_util
import module_sample_api.models.api_test_model as model
import json
import asyncio
import re
from io import BytesIO


# [그룹 서비스]
# (기본 요청 테스트 API)
async def basic_request_test(
        request: Request,
        response: Response
):
    return AppConf.server_profile


# ----
# (요청 Redirect 테스트 API)
async def redirect_test(
        request: Request,
        response: Response
):
    return RedirectResponse(url="/api-test")


# ----
# (Get 요청 테스트 (Query Parameter))
async def get_request_test(
        request: Request,
        response: Response,
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
    return model.GetRequestTestOutputVo(
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
    )


# ----
# (Get 요청 테스트 (Path Parameter))
async def get_request_test_with_path_param(
        request: Request,
        response: Response,
        path_param_int: int
):
    return model.GetRequestTestWithPathParamOutputVo(
        path_param_int=path_param_int
    )


# ----
# (Post 요청 테스트 (application-json))
async def post_request_test_with_application_json_type_request_body(
        request: Request,
        response: Response,
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBodyInputVo
):
    return model.PostRequestTestWithApplicationJsonTypeRequestBodyOutputVo(
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
    )


# ----
# (Post 요청 테스트 (application-json, 객체 파라미터 포함))
async def post_request_test_with_application_json_type_request_body2(
        request: Request,
        response: Response,
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

    return model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo(
        object_vo=object_vo_single,
        object_vo_list=object_vo_list
    )


# ----
# (Post 요청 테스트 (입출력값 없음))
async def post_request_test_with_no_input_and_output(
        request: Request,
        response: Response
):
    return None


# ----
# (Post 요청 테스트 (x-www-form-urlencoded))
async def post_request_test_with_form_type_request_body(
        request: Request,
        response: Response,
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
    return model.PostRequestTestWithFormTypeRequestBodyOutputVo(
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
    )


# ----
# (Post 요청 테스트 (multipart/form-data))
async def post_request_test_with_multipart_form_type_request_body(
        request: Request,
        response: Response,
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

    return model.PostRequestTestWithMultipartFormTypeRequestBodyOutputVo(
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
    )


# ----
# (Post 요청 테스트2 (multipart/form-data))
async def post_request_test_with_multipart_form_type_request_body2(
        request: Request,
        response: Response,
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
        multipart_file_list: List[UploadFile],
        multipart_file_list_nullable: Optional[List[UploadFile]]
):
    # 저장 경로 설정
    save_directory_path = os.path.abspath("./by_product_files/sample_api/test")

    # 파일 저장 (필수)
    for multipart_file in multipart_file_list:
        custom_util.multipart_file_local_save(save_directory_path, None, multipart_file)

    # 파일 저장 (nullable)
    if multipart_file_list_nullable is not None:
        for multipart_file_nullable in multipart_file_list_nullable:
            custom_util.multipart_file_local_save(save_directory_path, None, multipart_file_nullable)

    return model.PostRequestTestWithMultipartFormTypeRequestBody2OutputVo(
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
    )


# ----
# (Post 요청 테스트3 (multipart/form-data))
async def post_request_test_with_multipart_form_type_request_body3(
        request: Request,
        response: Response,
        json_string: str,
        multipart_file: UploadFile,
        multipart_file_nullable: Optional[UploadFile]
):
    # json_string 파싱
    input_json_object = model.PostRequestTestWithMultipartFormTypeRequestBody3InputVo(**json.loads(json_string))

    # 저장 경로 설정
    save_directory_path = os.path.abspath("./by_product_files/sample_api/test")

    # 파일 저장 (필수)
    custom_util.multipart_file_local_save(save_directory_path, None, multipart_file)

    # 파일 저장 (nullable)
    if multipart_file_nullable is not None:
        custom_util.multipart_file_local_save(save_directory_path, None, multipart_file_nullable)

    return model.PostRequestTestWithMultipartFormTypeRequestBody2OutputVo(
        request_form_string=input_json_object.request_form_string,
        request_form_string_nullable=input_json_object.request_form_string_nullable,
        request_form_int=input_json_object.request_form_int,
        request_form_int_nullable=input_json_object.request_form_int_nullable,
        request_form_double=input_json_object.request_form_double,
        request_form_double_nullable=input_json_object.request_form_double_nullable,
        request_form_boolean=input_json_object.request_form_boolean,
        request_form_boolean_nullable=input_json_object.request_form_boolean_nullable,
        request_form_string_list=input_json_object.request_form_string_list,
        request_form_string_list_nullable=input_json_object.request_form_string_list_nullable
    )


# ----
# (인위적 에러 발생 테스트)
async def generate_error_test(
        request: Request,
        response: Response
):
    raise Exception("Test Error")


# ----
# (결과 코드 발생 테스트)
async def return_result_code_through_headers(
        request: Request,
        response: Response,
        error_type: model.ReturnResultCodeThroughHeadersErrorTypeEnum
):
    if error_type is None:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_204_NO_CONTENT
        if error_type == model.ReturnResultCodeThroughHeadersErrorTypeEnum.A:
            response.headers["api-result-code"] = "1"
        elif error_type == model.ReturnResultCodeThroughHeadersErrorTypeEnum.B:
            response.headers["api-result-code"] = "2"
        elif error_type == model.ReturnResultCodeThroughHeadersErrorTypeEnum.C:
            response.headers["api-result-code"] = "3"
        return


# ----
# (인위적 응답 지연 테스트)
async def response_delay_test(request, response, delay_time_sec):
    end_time_ms = delay_time_sec * 1000
    wait_interval = 0.1  # 100ms

    elapsed = 0
    while elapsed < end_time_ms:
        await asyncio.sleep(wait_interval)
        elapsed += wait_interval * 1000  # 누적 시간 (ms)

    response.status_code = status.HTTP_200_OK
    return {"message": f"{delay_time_sec}초 지연 후 응답 완료"}


# ----
# (text/string 반환 샘플)
async def return_text_string_test(request, response):
    return PlainTextResponse("test Complete!", media_type="text/plain; charset=utf-8")


# ----
# (text/html 반환 샘플)
async def return_html_string_test(request, response):
    return AppConf.jinja2Templates.TemplateResponse(
        "return_text_html_test/html_response_example.html",
        {
            "request": request,
            "viewModel": {}
        }
    )


# ----
# (byte 반환 샘플)
async def return_byte_data_test(
        request: Request,
        response: Response,
        byte_range: Optional[str]
):
    full_data = bytearray([ord(c) for c in ['a', 'b', 'c', 'd', 'e', 'f']])

    start = 0
    end = len(full_data) - 1

    if byte_range:
        match = re.match(r"bytes=(\d+)-(\d+)", byte_range.lower())
        if match:
            start = int(match.group(1))
            end = int(match.group(2))

    partial_data = full_data[start:end + 1]

    # Set headers
    response.headers["Content-Range"] = f"bytes {start}-{end}/{len(full_data)}"
    response.headers["Accept-Ranges"] = "bytes"
    response.headers["Content-Length"] = str(len(partial_data))
    response.headers["Content-Type"] = "text/plain; charset=utf-8"

    return StreamingResponse(BytesIO(partial_data), media_type="text/plain")


# ----
# (비디오 스트리밍 샘플)
async def video_streaming_test(
        request: Request,
        response: Response,
        video_height: model.VideoStreamingTestVideoHeight
):
    # 모듈 루트 경로
    module_root_path = AppConf.module_folder_path

    # 비디오 파일 경로 구성
    base_path = os.path.join(module_root_path, "z_resources/static/video_streaming_test")

    file_name_map = {
        model.VideoStreamingTestVideoHeight.H240: "test_240p.mp4",
        model.VideoStreamingTestVideoHeight.H360: "test_360p.mp4",
        model.VideoStreamingTestVideoHeight.H480: "test_480p.mp4",
        model.VideoStreamingTestVideoHeight.H720: "test_720p.mp4",
    }

    file_name = file_name_map.get(video_height)
    full_path = os.path.join(base_path, file_name)

    # 미디어 응답 생성기 객체
    builder = custom_util.MediaStreamResponseBuilder(full_path)

    return await builder.build_response(request)


# ----
# (오디오 스트리밍 샘플)
async def audio_streaming_test(request, response):
    # 모듈 루트 경로
    module_root_path = AppConf.module_folder_path

    # 비디오 파일 경로 구성
    base_path = os.path.join(module_root_path, "z_resources/static/audio_streaming_test")

    file_name = "test.mp3"
    full_path = os.path.join(base_path, file_name)

    # 미디어 응답 생성기 객체
    builder = custom_util.MediaStreamResponseBuilder(full_path)

    return await builder.build_response(request)
