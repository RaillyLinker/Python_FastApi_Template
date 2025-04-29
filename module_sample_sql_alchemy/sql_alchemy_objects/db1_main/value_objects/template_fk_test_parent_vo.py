from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class FindAllFromTemplateFkTestParentWithNearestChildOnlyOutputVo(BaseModel):
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
    parent_create_date: datetime = (
        Field(
            ...,
            description="부모 테이블 행 생성일"
        )
    )
    parent_update_date: datetime = (
        Field(
            ...,
            description="부모 테이블 행 수정일"
        )
    )

    child_uid: Optional[int] = (
        Field(
            ...,
            description="자식 테이블 행 고유값"
        )
    )
    child_name: Optional[str] = (
        Field(
            ...,
            description="자식 테이블 이름"
        )
    )
    child_create_date: Optional[datetime] = (
        Field(
            ...,
            description="자식 테이블 행 생성일"
        )
    )
    child_update_date: Optional[datetime] = (
        Field(
            ...,
            description="자식 테이블 행 수정일"
        )
    )
