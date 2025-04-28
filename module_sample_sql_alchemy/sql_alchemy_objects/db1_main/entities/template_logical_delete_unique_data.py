from sqlalchemy import Column, Integer, String, BigInteger, DateTime, UniqueConstraint
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import Base


class Db1TemplateLogicalDeleteUniqueData(Base):
    __tablename__ = 'logical_delete_unique_data'
    __table_args__ = (
        UniqueConstraint(
            'unique_value', 'row_delete_date_str'
        ),
        {
            'schema': 'template',
            'comment': '논리적 삭제 유니크 제약 테스트 테이블'
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

    row_create_date = (
        Column(
            "row_create_date",
            DateTime(),
            nullable=False,
            comment="행 생성일"
        )
    )

    row_update_date = (
        Column(
            "row_update_date",
            DateTime(),
            nullable=False,
            comment="행 수정일"
        )
    )

    row_delete_date_str = (
        Column(
            "row_delete_date_str",
            String(50),
            nullable=False,
            comment="행 삭제일(yyyy_MM_dd_T_HH_mm_ss_SSS_z, 삭제되지 않았다면 /)"
        )
    )

    unique_value = (
        Column(
            "unique_value",
            Integer,
            nullable=False,
            comment="유니크 값"
        )
    )
