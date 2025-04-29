from pydantic import BaseModel, Field


class MultiCaseBooleanReturnTestOutputVo(BaseModel):
    normal_bool_value: int = (
        Field(
            ...,
            description="sql 에서 true 로 입력한 값"
        )
    )
    func_bool_value: int = (
        Field(
            ...,
            description="sql alchemy 레포지토리에서 입력한 값"
        )
    )
    if_bool_value: int = (
        Field(
            ...,
            description="sql if 문에서 반환된 값"
        )
    )
    case_bool_value: int = (
        Field(
            ...,
            description="sql case 문에서 반환된 값"
        )
    )
    table_column_bool_value: bool = (
        Field(
            ...,
            description="테이블 컬럼 반환값"
        )
    )
