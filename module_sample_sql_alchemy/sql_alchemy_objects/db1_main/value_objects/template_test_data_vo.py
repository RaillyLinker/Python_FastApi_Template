from pydantic import BaseModel, Field
from datetime import datetime


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
