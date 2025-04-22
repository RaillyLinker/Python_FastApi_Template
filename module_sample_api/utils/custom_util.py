import os
import shutil
import fastapi
from typing import Optional, Tuple
from datetime import datetime


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
        multipart_file: fastapi.UploadFile
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
        shutil.copyfileobj(multipart_file.file, f)

    return saved_file_name
