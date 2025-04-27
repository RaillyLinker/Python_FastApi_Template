from pydantic import BaseModel, Field
from datetime import datetime


# (입력값 거리 측정 쿼리)
class FindAllFromTemplateTestDataByNotDeletedWithRandomNumDistanceOutputVo(BaseModel):
    uid: int = (
        Field(
            ...,
            description="행 고유값"
        )
    )
    row_create_date: datetime = (
        Field(
            ...,
            description="행 생성일"
        )
    )
    row_update_date: datetime = (
        Field(
            ...,
            description="행 수정일"
        )
    )
    content: str = (
        Field(
            ...,
            description="테스트 본문"
        )
    )
    random_num: int = (
        Field(
            ...,
            description="테스트 랜덤 번호"
        )
    )
    test_datetime: datetime = (
        Field(
            ...,
            description="테스트용 일시 데이터"
        )
    )
    distance: int = (
        Field(
            ...,
            description="입력값과 랜덤 번호 간 거리"
        )
    )


# ----
# (입력값 거리 측정 쿼리)
class FindAllFromTemplateTestDataByNotDeletedWithRowCreateDateDistanceOutputVo(BaseModel):
    uid: int = (
        Field(
            ...,
            description="행 고유값"
        )
    )
    row_create_date: datetime = (
        Field(
            ...,
            description="행 생성일"
        )
    )
    row_update_date: datetime = (
        Field(
            ...,
            description="행 수정일"
        )
    )
    content: str = (
        Field(
            ...,
            description="테스트 본문"
        )
    )
    random_num: int = (
        Field(
            ...,
            description="테스트 랜덤 번호"
        )
    )
    test_datetime: datetime = (
        Field(
            ...,
            description="테스트용 일시 데이터"
        )
    )
    time_diff_micro_sec: int = (
        Field(
            ...,
            description="입력값과 생성일 간 거리"
        )
    )


# ----
# (네이티브 페이지네이션 샘플)
class FindPageAllFromTemplateTestDataByNotDeletedWithRandomNumDistanceOutputVo(BaseModel):
    uid: int = (
        Field(
            ...,
            description="행 고유값"
        )
    )
    row_create_date: datetime = (
        Field(
            ...,
            description="행 생성일"
        )
    )
    row_update_date: datetime = (
        Field(
            ...,
            description="행 수정일"
        )
    )
    content: str = (
        Field(
            ...,
            description="테스트 본문"
        )
    )
    random_num: int = (
        Field(
            ...,
            description="테스트 랜덤 번호"
        )
    )
    test_datetime: datetime = (
        Field(
            ...,
            description="테스트용 일시 데이터"
        )
    )
    distance: int = (
        Field(
            ...,
            description="입력값과 랜덤 번호 간 거리"
        )
    )


# ----
# (키워드 검색 샘플)
class FindPageAllFromTemplateTestDataBySearchKeywordOutputVo(BaseModel):
    uid: int = (
        Field(
            ...,
            description="행 고유값"
        )
    )
    row_create_date: datetime = (
        Field(
            ...,
            description="행 생성일"
        )
    )
    row_update_date: datetime = (
        Field(
            ...,
            description="행 수정일"
        )
    )
    content: str = (
        Field(
            ...,
            description="테스트 본문"
        )
    )
    random_num: int = (
        Field(
            ...,
            description="테스트 랜덤 번호"
        )
    )
    test_datetime: datetime = (
        Field(
            ...,
            description="테스트용 일시 데이터"
        )
    )
