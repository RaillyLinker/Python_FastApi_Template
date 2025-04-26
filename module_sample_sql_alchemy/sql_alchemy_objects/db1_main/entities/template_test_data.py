from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Db1TemplateTestData(Base):
    __tablename__ = 'test_data'
    __table_args__ = {
        'schema': 'template',
        'comment': '테스트 정보 테이블(논리적 삭제 적용)'
    }

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

    content = (
        Column(
            "content",
            String(255),
            nullable=False,
            comment="테스트 본문"
        )
    )

    random_num = (
        Column(
            "random_num",
            Integer,
            nullable=False,
            comment="테스트 랜덤 번호"
        )
    )

    test_datetime = (
        Column(
            "test_datetime",
            DateTime(),
            nullable=False,
            comment="테스트용 일시 데이터"
        )
    )
