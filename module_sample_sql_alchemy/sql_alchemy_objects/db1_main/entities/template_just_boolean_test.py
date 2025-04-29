from sqlalchemy import Column, Boolean, BigInteger
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import Base


class Db1TemplateJustBooleanTest(Base):
    __tablename__ = 'just_boolean_test'
    __table_args__ = (
        {
            'schema': 'template',
            'comment': 'Boolean 값 반환 예시만을 위한 테이블'
        }
    )

    uid = (
        Column(
            "uid",
            BigInteger,
            primary_key=True,
            autoincrement=True,
            comment="행 고유값"
        )
    )

    bool_value = (
        Column(
            "bool_value",
            Boolean,
            nullable=False,
            comment="bool 값"
        )
    )
