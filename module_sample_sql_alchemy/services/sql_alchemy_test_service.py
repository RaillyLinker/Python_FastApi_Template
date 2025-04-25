import os
from fastapi import UploadFile, Response, Request
from fastapi.responses import PlainTextResponse, StreamingResponse, FileResponse, JSONResponse
from typing import Optional, List
from fastapi.responses import RedirectResponse
from module_sample_sql_alchemy.configurations.app_conf import AppConf
import module_sample_sql_alchemy.utils.custom_util as custom_util
import module_sample_sql_alchemy.models.api_test_model as model
import json
import asyncio
import re
from io import BytesIO
from pathlib import Path as PathlibPath


# [그룹 서비스]
# (기본 요청 테스트 API)
async def basic_request_test(
        request: Request,
        response: Response
):
    return PlainTextResponse(
        status_code=200,
        content=AppConf.server_profile
    )
