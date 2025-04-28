from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import Base


class Db1TemplateFkTestManyToOneChild(Base):
    __tablename__ = "fk_test_many_to_one_child"
    __table_args__ = (
        {
            'schema': 'template',
            'comment': 'Foreign Key 테스트용 테이블 (one to many 테스트용 자식 테이블)'
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

    child_name = (
        Column(
            "child_name",
            String(255),
            nullable=False,
            comment="자식 테이블 이름"
        )
    )

    fk_test_parent_uid = (
        Column(
            "fk_test_parent_uid",
            BigInteger,
            ForeignKey("template.fk_test_parent.uid"),  # <-- ForeignKey 추가!
            nullable=False,
            comment="FK 부모 테이블 고유번호 (template.fk_test_parent.uid)"
        )
    )

    fk_test_parent = relationship(
        "Db1TemplateFkTestParent",
        back_populates="fk_test_many_to_one_child_list",
        lazy="select"
    )
