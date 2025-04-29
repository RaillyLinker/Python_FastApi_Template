import enum
from geoalchemy2 import Geometry
from sqlalchemy import (
    Column, BigInteger, String, DateTime, Enum, JSON, Boolean
)
from sqlalchemy.dialects.mysql import (
    TINYINT, MEDIUMINT, SMALLINT, DOUBLE, YEAR, SET, INTEGER, BIGINT, FLOAT, DECIMAL, DATE,
    DATETIME, TIME, TIMESTAMP, TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT, BIT, BINARY, VARBINARY, CHAR, VARCHAR
)
from module_sample_sql_alchemy.configurations.sql_alchemy.db1_main_config import Base


class EnumAbc(enum.Enum):
    A = "A"
    B = "B"
    C = "C"


class Db1TemplateDataTypeMappingTest(Base):
    __tablename__ = 'data_type_mapping_test'
    __table_args__ = (
        {
            'schema': 'template',
            'comment': 'ORM 과 Database 간 데이터 타입 매핑을 위한 테이블'
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

    # 숫자 데이터
    sample_tiny_int = (
        Column(
            "sample_tiny_int",
            TINYINT,
            nullable=False,
            comment="-128 ~ 127 정수 (1Byte)"
        )
    )
    sample_tiny_int_unsigned = (
        Column(
            "sample_tiny_int_unsigned",
            TINYINT(unsigned=True),
            nullable=False,
            comment="0 ~ 255 정수 (1Byte)"
        )
    )
    sample_small_int = (
        Column(
            "sample_small_int",
            SMALLINT,
            nullable=False,
            comment="-32,768 ~ 32,767 정수 (2Byte)"
        )
    )
    sample_small_int_unsigned = (
        Column(
            "sample_small_int_unsigned",
            SMALLINT(unsigned=True),
            nullable=False,
            comment="0 ~ 65,535 정수 (2Byte)"
        )
    )
    sample_medium_int = (
        Column(
            "sample_medium_int",
            MEDIUMINT,
            nullable=False,
            comment="-8,388,608 ~ 8,388,607 정수 (3Byte)"
        )
    )
    sample_medium_int_unsigned = (
        Column(
            "sample_medium_int_unsigned",
            MEDIUMINT(unsigned=True),
            nullable=False,
            comment="0 ~ 16,777,215 정수 (3Byte)"
        )
    )
    sample_int = (
        Column(
            "sample_int",
            INTEGER,
            nullable=False,
            comment="-2,147,483,648 ~ 2,147,483,647 정수 (4Byte)"
        )
    )
    sample_int_unsigned = (
        Column(
            "sample_int_unsigned",
            INTEGER(unsigned=True),
            nullable=False,
            comment="0 ~ 4,294,967,295 정수 (4Byte)"
        )
    )
    sample_big_int = (
        Column(
            "sample_big_int",
            BIGINT(),
            nullable=False,
            comment="-2^63 ~ 2^63-1 정수 (8Byte)"
        )
    )
    sample_big_int_unsigned = (
        Column(
            "sample_big_int_unsigned",
            BIGINT(unsigned=True),
            nullable=False,
            comment="0 ~ 2^64-1 정수 (8Byte)"
        )
    )
    sample_float = (
        Column(
            "sample_float",
            FLOAT(),
            nullable=False,
            comment="-3.4E38 ~ 3.4E38 단정밀도 부동소수점 (4Byte)"
        )
    )
    sample_float_unsigned = (
        Column(
            "sample_float_unsigned",
            FLOAT(unsigned=True),
            nullable=False,
            comment="0 ~ 3.402823466E+38 단정밀도 부동소수점 (4Byte)"
        )
    )
    sample_double = (
        Column(
            "sample_double",
            DOUBLE(),
            nullable=False,
            comment="-1.7E308 ~ 1.7E308 배정밀도 부동소수점 (8Byte)"
        )
    )
    sample_double_unsigned = (
        Column(
            "sample_double_unsigned",
            DOUBLE(unsigned=True),
            nullable=False,
            comment="0 ~ 1.7976931348623157E+308 배정밀도 부동소수점 (8Byte)"
        )
    )
    sample_decimal_p65_s10 = (
        Column(
            "sample_decimal_p65_s10",
            DECIMAL(65, 10),
            nullable=False,
            comment="p(전체 자릿수, 최대 65), s(소수점 아래 자릿수, p 보다 작거나 같아야 함) 설정 가능 고정 소수점 숫자"
        )
    )

    # 시간 데이터
    sample_date = (
        Column(
            "sample_date",
            DATE(),
            nullable=False,
            comment="1000-01-01 ~ 9999-12-31 날짜 데이터"
        )
    )
    sample_datetime = (
        Column(
            "sample_datetime",
            DATETIME(fsp=3),
            nullable=False,
            comment="1000-01-01 00:00:00 ~ 9999-12-31 23:59:59 날짜 데이터"
        )
    )
    sample_time = (
        Column(
            "sample_time",
            TIME(fsp=3),
            nullable=False,
            comment="-838:59:59 ~ 838:59:59 시간 데이터"
        )
    )
    sample_timestamp = (
        Column(
            "sample_timestamp",
            TIMESTAMP(fsp=3),
            nullable=False,
            comment="1970-01-01 00:00:01 ~ 2038-01-19 03:14:07 날짜 데이터 저장시 UTC 기준으로 저장되고, 조회시 시스템 설정에 맞게 반환"
        )
    )
    sample_year = (
        Column(
            "sample_year",
            YEAR(),
            nullable=False,
            comment="1901 ~ 2155 년도"
        )
    )

    # 문자 데이터
    sample_char12 = (
        Column(
            "sample_char12",
            CHAR(12),  # 명시적 CHAR
            nullable=False,
            comment="고정 길이 문자열 (최대 255 Byte), CHAR 타입은 항상 지정된 길이만큼 공간을 차지하며, 실제 저장되는 문자열이 그보다 짧으면 빈 공간으로 패딩하여 저장합니다."
        )
    )
    sample_varchar12 = (
        Column(
            "sample_varchar12",
            VARCHAR(12),  # 최대 12자 가변 길이 문자열
            nullable=False,
            comment="가변 길이 문자열 (최대 65,535 Byte), CHAR 과 달리 저장되는 데이터의 길이에 따라 실제 저장되는 공간이 달라집니다. "
                    "CHAR 에 비해 저장 공간 활용에 강점이 있고 성능에 미비한 약점이 있습니다."
        )
    )
    sample_tiny_text = (
        Column(
            "sample_tiny_text",
            TINYTEXT(),
            nullable=False,
            comment="가변 길이 문자열 최대 255 Byte"
        )
    )
    sample_text = (
        Column(
            "sample_text",
            TEXT(),
            nullable=False,
            comment="가변 길이 문자열 최대 65,535 Byte"
        )
    )
    sample_medium_text = (
        Column(
            "sample_medium_text",
            MEDIUMTEXT(),
            nullable=False,
            comment="가변 길이 문자열 최대 16,777,215 Byte"
        )
    )
    sample_long_text = (
        Column(
            "sample_long_text",
            LONGTEXT(),
            nullable=False,
            comment="가변 길이 문자열 최대 4,294,967,295 Byte"
        )
    )

    # Bit 데이터
    sample_one_bit = (
        Column(
            "sample_one_bit",
            Boolean(),
            nullable=False,
            comment="1 bit 값 (Boolean 으로 사용할 수 있습니다. (1 : 참, 0 : 거짓))"
        )
    )
    sample_6_bit = (
        Column(
            "sample_6_bit",
            BIT(6),  # 6비트 값을 저장하기 위한 Integer
            nullable=False,
            comment="n bit 값 (bit 사이즈에 따라 변수 사이즈를 맞춰 매핑)"
        )
    )

    # JSON 및 ENUM/SET
    sample_json = (
        Column(
            "sample_json",
            JSON(),
            nullable=True,
            comment="JSON 타입"
        )
    )
    sample_enum_abc = (
        Column(
            "sample_enum_abc",
            Enum(EnumAbc),
            nullable=False,
            comment="A, B, C 중 하나"
        )
    )
    sample_set_abc = (
        Column(
            "sample_set_abc",
            SET("A", "B", "C"),
            nullable=True
        )
    )

    # 공간 데이터 (GeoAlchemy2 필요)
    sample_geometry = (
        Column(
            "sample_geometry",
            Geometry(geometry_type='GEOMETRY'),
            nullable=False,
            comment="GEOMETRY 타입(Point, Line, Polygon 데이터 중 어느것이라도 하나를 넣을 수 있습니다.)"
        )
    )
    sample_point = (
        Column(
            "sample_point",
            Geometry(geometry_type='POINT'),
            nullable=False,
            comment="(X, Y) 공간 좌표"
        )
    )
    sample_linestring = (
        Column(
            "sample_linestring",
            Geometry(geometry_type='LINESTRING'),
            nullable=False,
            comment="직선의 시퀀스"
        )
    )
    sample_polygon = (
        Column(
            "sample_polygon",
            Geometry(geometry_type='POLYGON'),
            nullable=False,
            comment="다각형"
        )
    )

    # 바이너리
    sample_binary2 = (
        Column(
            "sample_binary2",
            BINARY(2),
            nullable=False,
            comment="고정 길이 이진 데이터 (최대 65535 바이트), 암호화된 값, UUID, 고정 길이 해시값 등을 저장하는 역할"
        )
    )
    sample_varbinary2 = (
        Column(
            "sample_varbinary2",
            VARBINARY(2),
            nullable=False,
            comment="가변 길이 이진 데이터 (최대 65535 바이트), 동적 크기의 바이너리 데이터, 이미지 등을 저장하는 역할"
        )
    )
