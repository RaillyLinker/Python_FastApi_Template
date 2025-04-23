from fastapi import APIRouter, Query, Path, Form, UploadFile, File, responses, Response, Request, Header
from fastapi.responses import PlainTextResponse, HTMLResponse
from typing import Optional, List
import module_sample_api.services.api_test_service as service
import module_sample_api.models.api_test_model as model

# [그룹 컨트롤러]
# Router 설정
router = APIRouter(
    prefix="/api-test",  # 전체 경로 앞에 붙는 prefix
    tags=["API 요청 / 응답에 대한 테스트 컨트롤러"]  # Swagger 문서 그룹 이름
)


# ----------------------------------------------------------------------------------------------------------------------
# <API 선언 공간>
@router.get(
    "",
    response_class=responses.PlainTextResponse,
    summary="기본 요청 테스트 API",
    description="이 API 를 요청하면 현재 실행중인 프로필 이름을 반환합니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def basic_request_test(
        request: Request,
        response: Response
):
    return await service.basic_request_test(request, response)


# ----
@router.get(
    "/redirect-to-blank",
    summary="요청 Redirect 테스트 API",
    description="이 API 를 요청하면 /api-test 로 Redirect 됩니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def redirect_test(
        request: Request,
        response: Response
):
    return await service.redirect_test(request, response)


# ----
@router.get(
    "/get-request",
    response_model=model.GetRequestTestOutputVo,
    summary="Get 요청 테스트 (Query Parameter)",
    description="Query Parameter 를 받는 Get 메소드 요청 테스트",
    responses={
        200: {"description": "OK"}
    }
)
async def get_request_test(
        request: Request,
        response: Response,
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
    return await service.get_request_test(
        request,
        response,
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
    responses={
        200: {"description": "OK"}
    }
)
async def get_request_test_with_path_param(
        request: Request,
        response: Response,
        path_param_int: int = Path(
            ...,
            alias="pathParamInt",
            description="Int Path 파라미터",
            example=1
        )
):
    return await service.get_request_test_with_path_param(request, response, path_param_int)


# ----
@router.post(
    "/post-request-application-json",
    response_model=model.PostRequestTestWithApplicationJsonTypeRequestBodyOutputVo,
    summary="Post 요청 테스트 (application-json)",
    description="application-json 형태의 Request Body 를 받는 Post 메소드 요청 테스트",
    responses={
        200: {"description": "OK"}
    }
)
async def post_request_test_with_application_json_type_request_body(
        request: Request,
        response: Response,
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBodyInputVo
):
    return await service.post_request_test_with_application_json_type_request_body(request, response, request_body)


# ----
@router.post(
    "/post-request-application-json-with-object-param",
    response_model=model.PostRequestTestWithApplicationJsonTypeRequestBody2OutputVo,
    summary="Post 요청 테스트 (application-json, 객체 파라미터 포함)",
    description="application-json 형태의 Request Body(객체 파라미터 포함) 를 받는 Post 메소드 요청 테스트",
    responses={
        200: {"description": "OK"}
    }
)
async def post_request_test_with_application_json_type_request_body2(
        request: Request,
        response: Response,
        request_body: model.PostRequestTestWithApplicationJsonTypeRequestBody2InputVo
):
    return await service.post_request_test_with_application_json_type_request_body2(request, response, request_body)


# ----
@router.post(
    "/post-request-application-json-with-no-param",
    summary="Post 요청 테스트 (입출력값 없음)",
    description="입출력값이 없는 Post 메소드 요청 테스트",
    responses={
        200: {"description": "OK"}
    }
)
async def post_request_test_with_no_input_and_output(
        request: Request,
        response: Response
):
    return await service.post_request_test_with_no_input_and_output(request, response)


# ----
@router.post(
    "/post-request-x-www-form-urlencoded",
    response_model=model.PostRequestTestWithFormTypeRequestBodyOutputVo,
    summary="Post 요청 테스트 (x-www-form-urlencoded)",
    description="x-www-form-urlencoded 형태의 Request Body 를 받는 Post 메소드 요청 테스트",
    responses={
        200: {"description": "OK"}
    }
)
async def post_request_test_with_form_type_request_body(
        request: Request,
        response: Response,
        request_form_string: str =
        Form(
            ...,
            alias="requestFormString",
            validation_alias="requestFormString",
            description="String Form 파라미터",
            examples=["testString"]
        ),
        request_form_string_nullable: Optional[str] =
        Form(
            None,
            alias="requestFormStringNullable",
            validation_alias="requestFormStringNullable",
            description="String Nullable Form 파라미터",
            examples=["testString"]
        ),
        request_form_int: int =
        Form(
            ...,
            alias="requestFormInt",
            validation_alias="requestFormInt",
            description="Int Form 파라미터",
            examples=[1]
        ),
        request_form_int_nullable: Optional[int] =
        Form(
            None,
            alias="requestFormIntNullable",
            validation_alias="requestFormIntNullable",
            description="Int Nullable Form 파라미터",
            examples=[1]
        ),
        request_form_double: float =
        Form(
            ...,
            alias="requestFormDouble",
            validation_alias="requestFormDouble",
            description="Double Form 파라미터",
            examples=[1.1]
        ),
        request_form_double_nullable: Optional[float] =
        Form(
            None,
            alias="requestFormDoubleNullable",
            validation_alias="requestFormDoubleNullable",
            description="Double Nullable Form 파라미터",
            examples=[1.1]
        ),
        request_form_boolean: bool =
        Form(
            ...,
            alias="requestFormBoolean",
            validation_alias="requestFormBoolean",
            description="Boolean Form 파라미터",
            examples=[True]
        ),
        request_form_boolean_nullable: Optional[bool] =
        Form(
            None,
            alias="requestFormBooleanNullable",
            validation_alias="requestFormBooleanNullable",
            description="Boolean Nullable Form 파라미터",
            examples=[True]
        ),
        request_form_string_list: List[str] =
        Form(
            ...,
            alias="requestFormStringList",
            validation_alias="requestFormStringList",
            description="StringList Form 파라미터",
            examples=[["testString1", "testString2"]]
        ),
        request_form_string_list_nullable: Optional[List[str]] =
        Form(
            None,
            alias="requestFormStringListNullable",
            validation_alias="requestFormStringListNullable",
            description="StringList Nullable Form 파라미터",
            examples=[["testString1", "testString2"]]
        )
):
    return await service.post_request_test_with_form_type_request_body(
        request,
        response,
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


# ----
@router.post(
    "/post-request-multipart-form-data",
    response_model=model.PostRequestTestWithMultipartFormTypeRequestBodyOutputVo,
    summary="Post 요청 테스트 (multipart/form-data)",
    description="multipart/form-data 형태의 Request Body 를 받는 Post 메소드 요청 테스트<br>"
                "MultipartFile 파라미터가 null 이 아니라면 저장",
    responses={
        200: {"description": "OK"}
    }
)
async def post_request_test_with_multipart_form_type_request_body(
        request: Request,
        response: Response,
        request_form_string: str =
        Form(
            ...,
            alias="requestFormString",
            validation_alias="requestFormString",
            description="String Form 파라미터",
            examples=["testString"]
        ),
        request_form_string_nullable: Optional[str] =
        Form(
            None,
            alias="requestFormStringNullable",
            validation_alias="requestFormStringNullable",
            description="String Nullable Form 파라미터",
            examples=["testString"]
        ),
        request_form_int: int =
        Form(
            ...,
            alias="requestFormInt",
            validation_alias="requestFormInt",
            description="Int Form 파라미터",
            examples=[1]
        ),
        request_form_int_nullable: Optional[int] =
        Form(
            None,
            alias="requestFormIntNullable",
            validation_alias="requestFormIntNullable",
            description="Int Nullable Form 파라미터",
            examples=[1]
        ),
        request_form_double: float =
        Form(
            ...,
            alias="requestFormDouble",
            validation_alias="requestFormDouble",
            description="Double Form 파라미터",
            examples=[1.1]
        ),
        request_form_double_nullable: Optional[float] =
        Form(
            None,
            alias="requestFormDoubleNullable",
            validation_alias="requestFormDoubleNullable",
            description="Double Nullable Form 파라미터",
            examples=[1.1]
        ),
        request_form_boolean: bool =
        Form(
            ...,
            alias="requestFormBoolean",
            validation_alias="requestFormBoolean",
            description="Boolean Form 파라미터",
            examples=[True]
        ),
        request_form_boolean_nullable: Optional[bool] =
        Form(
            None,
            alias="requestFormBooleanNullable",
            validation_alias="requestFormBooleanNullable",
            description="Boolean Nullable Form 파라미터",
            examples=[True]
        ),
        request_form_string_list: List[str] =
        Form(
            ...,
            alias="requestFormStringList",
            validation_alias="requestFormStringList",
            description="StringList Form 파라미터",
            examples=[["testString1", "testString2"]]
        ),
        request_form_string_list_nullable: Optional[List[str]] =
        Form(
            None,
            alias="requestFormStringListNullable",
            validation_alias="requestFormStringListNullable",
            description="StringList Nullable Form 파라미터",
            examples=[["testString1", "testString2"]]
        ),
        multipart_file: UploadFile =
        File(
            ...,
            alias="multipartFile",
            validation_alias="multipartFile",
            description="멀티 파트 파일"
        ),
        multipart_file_nullable: Optional[UploadFile] =
        File(
            None,
            alias="multipartFileNullable",
            validation_alias="multipartFileNullable",
            description="멀티 파트 파일 Nullable"
        ),
):
    return await service.post_request_test_with_multipart_form_type_request_body(
        request,
        response,
        request_form_string,
        request_form_string_nullable,
        request_form_int,
        request_form_int_nullable,
        request_form_double,
        request_form_double_nullable,
        request_form_boolean,
        request_form_boolean_nullable,
        request_form_string_list,
        request_form_string_list_nullable,
        multipart_file,
        multipart_file_nullable
    )


# ----
@router.post(
    "/post-request-multipart-form-data2",
    response_model=model.PostRequestTestWithMultipartFormTypeRequestBody2OutputVo,
    summary="Post 요청 테스트2 (multipart/form-data)",
    description="multipart/form-data 형태의 Request Body 를 받는 Post 메소드 요청 테스트(Multipart File List)<br>"
                "파일 리스트가 null 이 아니라면 저장",
    responses={
        200: {"description": "OK"}
    }
)
async def post_request_test_with_multipart_form_type_request_body2(
        request: Request,
        response: Response,
        request_form_string: str =
        Form(
            ...,
            alias="requestFormString",
            validation_alias="requestFormString",
            description="String Form 파라미터",
            examples=["testString"]
        ),
        request_form_string_nullable: Optional[str] =
        Form(
            None,
            alias="requestFormStringNullable",
            validation_alias="requestFormStringNullable",
            description="String Nullable Form 파라미터",
            examples=["testString"]
        ),
        request_form_int: int =
        Form(
            ...,
            alias="requestFormInt",
            validation_alias="requestFormInt",
            description="Int Form 파라미터",
            examples=[1]
        ),
        request_form_int_nullable: Optional[int] =
        Form(
            None,
            alias="requestFormIntNullable",
            validation_alias="requestFormIntNullable",
            description="Int Nullable Form 파라미터",
            examples=[1]
        ),
        request_form_double: float =
        Form(
            ...,
            alias="requestFormDouble",
            validation_alias="requestFormDouble",
            description="Double Form 파라미터",
            examples=[1.1]
        ),
        request_form_double_nullable: Optional[float] =
        Form(
            None,
            alias="requestFormDoubleNullable",
            validation_alias="requestFormDoubleNullable",
            description="Double Nullable Form 파라미터",
            examples=[1.1]
        ),
        request_form_boolean: bool =
        Form(
            ...,
            alias="requestFormBoolean",
            validation_alias="requestFormBoolean",
            description="Boolean Form 파라미터",
            examples=[True]
        ),
        request_form_boolean_nullable: Optional[bool] =
        Form(
            None,
            alias="requestFormBooleanNullable",
            validation_alias="requestFormBooleanNullable",
            description="Boolean Nullable Form 파라미터",
            examples=[True]
        ),
        request_form_string_list: List[str] =
        Form(
            ...,
            alias="requestFormStringList",
            validation_alias="requestFormStringList",
            description="StringList Form 파라미터",
            examples=[["testString1", "testString2"]]
        ),
        request_form_string_list_nullable: Optional[List[str]] =
        Form(
            None,
            alias="requestFormStringListNullable",
            validation_alias="requestFormStringListNullable",
            description="StringList Nullable Form 파라미터",
            examples=[["testString1", "testString2"]]
        ),
        multipart_file_list: List[UploadFile] =
        File(
            ...,
            alias="multipartFile",
            validation_alias="multipartFile",
            description="멀티 파트 파일"
        ),
        multipart_file_list_nullable: Optional[List[UploadFile]] =
        File(
            None,
            alias="multipartFileNullable",
            validation_alias="multipartFileNullable",
            description="멀티 파트 파일 Nullable"
        ),
):
    return await service.post_request_test_with_multipart_form_type_request_body2(
        request,
        response,
        request_form_string,
        request_form_string_nullable,
        request_form_int,
        request_form_int_nullable,
        request_form_double,
        request_form_double_nullable,
        request_form_boolean,
        request_form_boolean_nullable,
        request_form_string_list,
        request_form_string_list_nullable,
        multipart_file_list,
        multipart_file_list_nullable
    )


# ----
@router.post(
    "/post-request-multipart-form-data-json",
    response_model=model.PostRequestTestWithMultipartFormTypeRequestBody3OutputVo,
    summary="Post 요청 테스트3 (multipart/form-data - JsonString)",
    description="multipart/form-data 형태의 Request Body 를 받는 Post 메소드 요청 테스트<br>"
                "Form Data 의 Input Body 에는 Object 리스트 타입은 사용 불가능입니다.<br>"
                "Object 리스트 타입을 사용한다면, Json String 타입으로 객체를 받아서 파싱하여 사용하는 방식을 사용합니다.<br>"
                "아래 예시에서는 모두 JsonString 형식으로 만들었지만, ObjectList 타입만 이런식으로 처리하세요.",
    responses={
        200: {"description": "OK"}
    }
)
async def post_request_test_with_multipart_form_type_request_body3(
        request: Request,
        response: Response,
        json_string: str =
        Form(
            ...,
            alias="jsonString",
            validation_alias="jsonString",
            description="""
                class PostRequestTestWithMultipartFormTypeRequestBody3InputVo():
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
                    """,
            examples=["""
            {
                "requestFormString": "testString",
                "requestFormStringNullable": null,
                "requestFormInt": 1,
                "requestFormIntNullable": null,
                "requestFormDouble": 1.1,
                "requestFormDoubleNullable": null,
                "requestFormBoolean": true,
                "requestFormBooleanNullable": null,
                "requestFormStringList": [
                    "testString1",
                    "testString2"
                ],
                "requestFormStringListNullable": null
            }
            """]
        ),
        multipart_file: UploadFile =
        File(
            ...,
            alias="multipartFile",
            validation_alias="multipartFile",
            description="멀티 파트 파일"
        ),
        multipart_file_nullable: Optional[UploadFile] =
        File(
            None,
            alias="multipartFileNullable",
            validation_alias="multipartFileNullable",
            description="멀티 파트 파일 Nullable"
        ),
):
    return await service.post_request_test_with_multipart_form_type_request_body3(
        request,
        response,
        json_string,
        multipart_file,
        multipart_file_nullable
    )


# ----
@router.post(
    "/generate-error",
    summary="인위적 에러 발생 테스트",
    description="요청 받으면 인위적인 서버 에러를 발생시킵니다.(Http Response Status 500)",
    responses={
        200: {"description": "OK"}
    }
)
async def generate_error_test(
        request: Request,
        response: Response
):
    return await service.generate_error_test(request, response)


# ----
@router.post(
    "/api-result-code-test",
    summary="결과 코드 발생 테스트",
    description="Response Header 에 api-result-code 를 반환하는 테스트 API",
    responses={
        200: {"description": "OK"},
        204: {
            "description": "Response Body 가 없습니다.<br>Response Headers 를 확인하세요.",
            "headers": {
                "api-result-code": {
                    "description": "(Response Code 반환 원인) - Required<br>"
                                   "1 : errorType 을 A 로 보냈습니다.<br>"
                                   "2 : errorType 을 B 로 보냈습니다.<br>"
                                   "3 : errorType 을 C 로 보냈습니다.",
                    "schema": {
                        "type": "string"
                    }
                }
            }
        }
    }
)
async def return_result_code_through_headers(
        request: Request,
        response: Response,
        error_type: model.ReturnResultCodeThroughHeadersErrorTypeEnum =
        Query(
            default=None,
            alias="errorType",
            description="정상적이지 않은 상황을 만들도록 가정된 변수입니다.",
            example="A"
        )
):
    return await service.return_result_code_through_headers(request, response, error_type)


# ----
@router.post(
    "/time-delay-test",
    summary="인위적 응답 지연 테스트",
    description="임의로 응답 시간을 지연시킵니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def response_delay_test(
        request: Request,
        response: Response,
        delay_time_sec: int =
        Query(
            ...,
            alias="delayTimeSec",
            description="지연 시간(초)",
            example=1
        )
):
    return await service.response_delay_test(request, response, delay_time_sec)


# ----
@router.get(
    "/return-text-string",
    response_class=PlainTextResponse,
    summary="text/string 반환 샘플",
    description="text/string 형식의 Response Body 를 반환합니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def return_text_string_test(
        request: Request,
        response: Response
):
    return await service.return_text_string_test(request, response)


# ----
@router.get(
    "/return-text-html",
    response_class=HTMLResponse,
    summary="text/html 반환 샘플",
    description="text/html 형식의 Response Body 를 반환합니다.",
    responses={
        200: {"description": "OK"}
    }
)
async def return_html_string_test(
        request: Request,
        response: Response
):
    return await service.return_html_string_test(request, response)


# ----
@router.get(
    "/byte",
    summary="byte 반환 샘플",
    response_class=PlainTextResponse,
    description=(
            "byte array('a', .. , 'f') 에서 아래와 같은 요청으로 원하는 바이트를 요청 가능<br>"
            ">> curl http://localhost:12006/byte -i -H \"byteRange: bytes=2-4\""
    ),
    responses={
        200: {"description": "OK"}
    }
)
async def return_byte_data_test(
        request: Request,
        response: Response,
        byte_range: str =
        Header(
            None,
            alias="byteRange",
            description="byte array('a', 'b', 'c', 'd', 'e', 'f') 중 가져올 범위(0 부터 시작되는 인덱스)",
            example="bytes=2-4"
        )
):
    return await service.return_byte_data_test(request, response, byte_range)
