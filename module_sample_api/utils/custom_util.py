import os
from shutil import copyfileobj
from fastapi import UploadFile, Request, HTTPException
from typing import Optional, Tuple, AsyncGenerator
from datetime import datetime
from fastapi.responses import StreamingResponse
import mimetypes
import asyncio


# (파일명, 경로, 확장자 분리 함수)
# sample.jpg -> sample, jpg
def split_file_path(file_path: str) -> Tuple[str, Optional[str]]:
    file_name = os.path.splitext(file_path)[0]  # 확장자를 제외한 파일명
    extension = os.path.splitext(file_path)[1][1:] if '.' in file_path else None  # 확장자 (없으면 None)
    return file_name, extension


# (Multipart File을 로컬에 저장)
# 반환값 : 저장된 파일명
def multipart_file_local_save(
        # 파일을 저장할 로컬 위치 Path
        save_directory_path: str,
        # 저장할 파일명(파일명 뒤에 (현재 일시 yyyy_MM_dd_'T'_HH_mm_ss_SSS_z) 가 붙습니다.)
        # null 이라면 multipartFile 의 originalFilename 을 사용합니다.
        file_name: Optional[str],
        # 저장할 MultipartFile
        multipart_file: UploadFile
) -> str:
    # 파일 저장 기본 디렉토리 생성
    os.makedirs(save_directory_path, exist_ok=True)

    # 원본 파일명(with suffix)
    multi_part_file_name_string = multipart_file.filename

    # 확장자 분리
    file_name_split, file_extension = split_file_path(multi_part_file_name_string)

    # 확장자가 없는 파일명
    file_name_with_out_extension = file_name if file_name else file_name_split
    # 확장자
    file_extension = f".{file_extension}" if file_extension else ""

    # 파일명에 날짜/시간 추가
    saved_file_name = \
        f"{file_name_with_out_extension}({datetime.now().strftime('%Y_%m_%d_T%H_%M_%S_%f')}){file_extension}"

    # multipartFile을 targetPath에 저장
    target_path = os.path.join(save_directory_path, saved_file_name)
    with open(target_path, 'wb') as f:
        copyfileobj(multipart_file.file, f)

    return saved_file_name


# (비디오 스트리밍 처리)
# 비동기 비디오 스트리밍 응답 생성기
class VideoStreamResponseBuilder:
    def __init__(self, file_path: str, chunk_size: int = 1024 * 1024):
        self.file_path = file_path
        self.chunk_size = chunk_size

        if not os.path.isfile(self.file_path):
            raise HTTPException(status_code=404, detail="Video file not found")

        self.file_size = os.path.getsize(self.file_path)
        self.content_type = mimetypes.guess_type(self.file_path)[0] or "application/octet-stream"

    async def _file_chunk_generator(self, start: int = 0, end: Optional[int] = None) -> AsyncGenerator[bytes, None]:
        loop = asyncio.get_event_loop()
        with open(self.file_path, "rb") as f:
            f.seek(start)
            remaining = (end - start + 1) if end else None

            while True:
                chunk_size = self.chunk_size if not remaining else min(self.chunk_size, remaining)
                data = await loop.run_in_executor(None, f.read, chunk_size)
                if not data:
                    break
                yield data
                if remaining:
                    remaining -= len(data)
                    if remaining <= 0:
                        break

    async def build_response(self, request: Request) -> StreamingResponse:
        range_header = request.headers.get("range")

        if range_header:
            range_value = range_header.strip().lower().replace("bytes=", "")
            try:
                range_start_str, range_end_str = range_value.split("-")
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid Range header format")
            range_start = int(range_start_str)
            range_end = int(range_end_str) if range_end_str.strip() else self.file_size - 1

            if range_start > range_end or range_end >= self.file_size:
                raise HTTPException(status_code=416, detail="Requested Range Not Satisfiable")

            content_length = range_end - range_start + 1

            headers = {
                "Content-Range": f"bytes {range_start}-{range_end}/{self.file_size}",
                "Accept-Ranges": "bytes",
                "Content-Length": str(content_length),
                "Content-Type": self.content_type,
            }

            return StreamingResponse(
                content=self._file_chunk_generator(range_start, range_end),
                status_code=206,
                headers=headers,
            )

        # Full file streaming
        headers = {
            "Accept-Ranges": "bytes",
            "Content-Length": str(self.file_size),
            "Content-Type": self.content_type,
        }

        return StreamingResponse(
            content=self._file_chunk_generator(),
            headers=headers,
        )
