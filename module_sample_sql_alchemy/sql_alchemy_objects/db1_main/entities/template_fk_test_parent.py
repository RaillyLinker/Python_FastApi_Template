from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.orm import relationship
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import Base


class Db1TemplateFkTestParent(Base):
    __tablename__ = "fk_test_parent"
    __table_args__ = (
        {
            'schema': 'template',
            'comment': 'Foreign Key 테스트용 테이블 (부모 테이블)'
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

    parent_name = (
        Column(
            "parent_name",
            String(255),
            nullable=False,
            comment="부모 테이블 이름"
        )
    )

    fk_test_many_to_one_child_list = (
        relationship(
            "Db1TemplateFkTestManyToOneChild",
            back_populates="fk_test_parent",
            cascade="all, delete-orphan",
            lazy="select"
        )
    )
