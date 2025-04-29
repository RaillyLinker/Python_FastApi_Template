from pydantic import BaseModel, Field
from datetime import datetime


class FindAllFromTemplateFkTestManyToOneChildInnerJoinParentByNotDeletedOutputVo(BaseModel):
    child_uid: int = (
        Field(
            ...,
            description="자식 테이블 행 고유값"
        )
    )
    child_name: str = (
        Field(
            ...,
            description="자식 테이블 이름"
        )
    )
    child_create_date: datetime = (
        Field(
            ...,
            description="자식 테이블 행 생성일"
        )
    )
    child_update_date: datetime = (
        Field(
            ...,
            description="자식 테이블 행 수정일"
        )
    )
    parent_uid: int = (
        Field(
            ...,
            description="부모 테이블 행 고유값"
        )
    )
    parent_name: str = (
        Field(
            ...,
            description="부모 테이블 이름"
        )
    )
