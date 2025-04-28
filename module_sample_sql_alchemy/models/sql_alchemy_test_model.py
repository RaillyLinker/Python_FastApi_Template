from pydantic import BaseModel, Field
from typing import List


# [그룹 모델]
# (DB Row 입력 테스트 API)
class PostInsertDataSampleInputVo(BaseModel):
    class Config:
        validate_by_name = True

    content: str = (
        Field(
            ...,
            alias="content",
            description="글 본문",
            examples=["테스트 텍스트입니다."]
        )
    )
    date_string: str = (
        Field(
            ...,
            alias="dateString",
            description="원하는 날짜(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )


class PostInsertDataSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    uid: int = (
        Field(
            ...,
            alias="uid",
            description="글 고유번호",
            examples=[1]
        )
    )
    create_date: str = (
        Field(
            ...,
            alias="createDate",
            description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    update_date: str = (
        Field(
            ...,
            alias="updateDate",
            description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    delete_date: str = (
        Field(
            ...,
            alias="deleteDate",
            description="글 삭제일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z, Null 이면 /)",
            examples=["/"]
        )
    )
    content: str = (
        Field(
            ...,
            alias="content",
            description="글 본문",
            examples=["테스트 텍스트입니다."]
        )
    )
    random_num: int = (
        Field(
            ...,
            alias="randomNum",
            description="자동 생성 숫자",
            examples=[1]
        )
    )
    test_datetime: str = (
        Field(
            ...,
            alias="testDatetime",
            description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )


# ----
# (DB Rows 조회 테스트 API)
class GetSelectRowsSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class TestEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        delete_date: str = (
            Field(
                ...,
                alias="deleteDate",
                description="글 삭제일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z, Null 이면 /)",
                examples=["/"]
            )
        )
        content: str = (
            Field(
                ...,
                alias="content",
                description="글 본문",
                examples=["테스트 텍스트입니다."]
            )
        )
        random_num: int = (
            Field(
                ...,
                alias="randomNum",
                description="자동 생성 숫자",
                examples=[1]
            )
        )
        test_datetime: str = (
            Field(
                ...,
                alias="testDatetime",
                description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )

    test_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="testEntityVoList",
            description="아이템 리스트"
        )
    )

    logical_delete_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="logicalDeleteEntityVoList",
            description="논리적으로 제거된 아이템 리스트"
        )
    )


# ----
# (DB 테이블의 random_num 컬럼 근사치 기준으로 정렬한 리스트 조회 API)
class GetRowsOrderByRandomNumSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class TestEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        content: str = (
            Field(
                ...,
                alias="content",
                description="글 본문",
                examples=["테스트 텍스트입니다."]
            )
        )
        random_num: int = (
            Field(
                ...,
                alias="randomNum",
                description="자동 생성 숫자",
                examples=[1]
            )
        )
        test_datetime: str = (
            Field(
                ...,
                alias="testDatetime",
                description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        distance: int = (
            Field(
                ...,
                alias="distance",
                description="기준과의 절대거리",
                examples=[1]
            )
        )

    test_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="testEntityVoList",
            description="아이템 리스트"
        )
    )


# ----
# (DB 테이블의 random_num 컬럼 근사치 기준으로 정렬한 리스트 조회 API)
class GetRowsOrderByRowCreateDateSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class TestEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        content: str = (
            Field(
                ...,
                alias="content",
                description="글 본문",
                examples=["테스트 텍스트입니다."]
            )
        )
        random_num: int = (
            Field(
                ...,
                alias="randomNum",
                description="자동 생성 숫자",
                examples=[1]
            )
        )
        test_datetime: str = (
            Field(
                ...,
                alias="testDatetime",
                description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        time_diff_micro_sec: int = (
            Field(
                ...,
                alias="timeDiffMicroSec",
                description="기준과의 절대차이(마이크로 초)",
                examples=[1]
            )
        )

    test_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="testEntityVoList",
            description="아이템 리스트"
        )
    )


# ----
# (DB Rows 조회 테스트 (페이징))
class GetRowsPageSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class TestEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        content: str = (
            Field(
                ...,
                alias="content",
                description="글 본문",
                examples=["테스트 텍스트입니다."]
            )
        )
        random_num: int = (
            Field(
                ...,
                alias="randomNum",
                description="자동 생성 숫자",
                examples=[1]
            )
        )
        test_datetime: str = (
            Field(
                ...,
                alias="testDatetime",
                description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )

    total_elements: int = (
        Field(
            ...,
            alias="totalElements",
            description="아이템 전체 개수",
            examples=[1]
        )
    )

    test_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="testEntityVoList",
            description="아이템 리스트"
        )
    )


# ----
# (DB Rows 조회 테스트 (네이티브 쿼리 페이징))
class GetRowsNativeQueryPageSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class TestEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        content: str = (
            Field(
                ...,
                alias="content",
                description="글 본문",
                examples=["테스트 텍스트입니다."]
            )
        )
        random_num: int = (
            Field(
                ...,
                alias="randomNum",
                description="자동 생성 숫자",
                examples=[1]
            )
        )
        test_datetime: str = (
            Field(
                ...,
                alias="testDatetime",
                description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        distance: int = (
            Field(
                ...,
                alias="distance",
                description="기준과의 절대거리",
                examples=[1]
            )
        )

    total_elements: int = (
        Field(
            ...,
            alias="totalElements",
            description="아이템 전체 개수",
            examples=[1]
        )
    )

    test_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="testEntityVoList",
            description="아이템 리스트"
        )
    )


# ----
# (DB Row 수정 테스트 API)
class PutRowSampleInputVo(BaseModel):
    class Config:
        validate_by_name = True

    content: str = (
        Field(
            ...,
            alias="content",
            description="글 본문",
            examples=["테스트 텍스트 수정글입니다."]
        )
    )
    date_string: str = (
        Field(
            ...,
            alias="dateString",
            description="원하는 날짜(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )


class PutRowSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    uid: int = (
        Field(
            ...,
            alias="uid",
            description="글 고유번호",
            examples=[1]
        )
    )
    create_date: str = (
        Field(
            ...,
            alias="createDate",
            description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    update_date: str = (
        Field(
            ...,
            alias="updateDate",
            description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    content: str = (
        Field(
            ...,
            alias="content",
            description="글 본문",
            examples=["테스트 텍스트입니다."]
        )
    )
    random_num: int = (
        Field(
            ...,
            alias="randomNum",
            description="자동 생성 숫자",
            examples=[1]
        )
    )
    test_datetime: str = (
        Field(
            ...,
            alias="testDatetime",
            description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )


# ----
# (DB Row 수정 테스트 (ORM))
class PutRowOrmSampleInputVo(BaseModel):
    class Config:
        validate_by_name = True

    content: str = (
        Field(
            ...,
            alias="content",
            description="글 본문",
            examples=["테스트 텍스트 수정글입니다."]
        )
    )
    date_string: str = (
        Field(
            ...,
            alias="dateString",
            description="원하는 날짜(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )


# ----
# (DB 정보 검색 테스트)
class GetRowWhereSearchingKeywordSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class TestEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        content: str = (
            Field(
                ...,
                alias="content",
                description="글 본문",
                examples=["테스트 텍스트입니다."]
            )
        )
        random_num: int = (
            Field(
                ...,
                alias="randomNum",
                description="자동 생성 숫자",
                examples=[1]
            )
        )
        test_datetime: str = (
            Field(
                ...,
                alias="testDatetime",
                description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )

    total_elements: int = (
        Field(
            ...,
            alias="totalElements",
            description="아이템 전체 개수",
            examples=[1]
        )
    )

    test_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="testEntityVoList",
            description="아이템 리스트"
        )
    )


# ----
# (DB Rows 조회 테스트 (카운팅))
class GetRowsCountSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    total_elements: int = (
        Field(
            ...,
            alias="totalElements",
            description="아이템 전체 개수",
            examples=[1]
        )
    )


# ----
# (DB Rows 조회 테스트 (네이티브 카운팅))
class GetRowsCountByNativeQuerySample(BaseModel):
    class Config:
        validate_by_name = True

    total_elements: int = (
        Field(
            ...,
            alias="totalElements",
            description="아이템 전체 개수",
            examples=[1]
        )
    )


# ----
# (DB Row 조회 테스트 (네이티브))
class GetRowByNativeQuerySampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    uid: int = (
        Field(
            ...,
            alias="uid",
            description="글 고유번호",
            examples=[1]
        )
    )
    create_date: str = (
        Field(
            ...,
            alias="createDate",
            description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    update_date: str = (
        Field(
            ...,
            alias="updateDate",
            description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    content: str = (
        Field(
            ...,
            alias="content",
            description="글 본문",
            examples=["테스트 텍스트입니다."]
        )
    )
    random_num: int = (
        Field(
            ...,
            alias="randomNum",
            description="자동 생성 숫자",
            examples=[1]
        )
    )
    test_datetime: str = (
        Field(
            ...,
            alias="testDatetime",
            description="테스트용 일시 데이터(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )


# ----
# (DB Row 입력 테스트 API)
class PostUniqueTestTableRowSampleInputVo(BaseModel):
    class Config:
        validate_by_name = True

    unique_value: int = (
        Field(
            ...,
            alias="uniqueValue",
            description="유니크 값",
            examples=[1]
        )
    )


class PostUniqueTestTableRowSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    uid: int = (
        Field(
            ...,
            alias="uid",
            description="글 고유번호",
            examples=[1]
        )
    )
    create_date: str = (
        Field(
            ...,
            alias="createDate",
            description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    update_date: str = (
        Field(
            ...,
            alias="updateDate",
            description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    delete_date: str = (
        Field(
            ...,
            alias="deleteDate",
            description="글 삭제일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z, Null 이면 /)",
            examples=["/"]
        )
    )
    unique_value: int = (
        Field(
            ...,
            alias="uniqueValue",
            description="유니크 값",
            examples=[1]
        )
    )


# ----
# (유니크 테스트 테이블 Rows 조회 테스트)
class GetUniqueTestTableRowsSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class TestEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        delete_date: str = (
            Field(
                ...,
                alias="deleteDate",
                description="글 삭제일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z, Null 이면 /)",
                examples=["/"]
            )
        )
        unique_value: int = (
            Field(
                ...,
                alias="uniqueValue",
                description="유니크 값",
                examples=[1]
            )
        )

    test_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="testEntityVoList",
            description="아이템 리스트"
        )
    )

    logical_delete_entity_vo_list: List[TestEntityVo] = (
        Field(
            ...,
            alias="logicalDeleteEntityVoList",
            description="논리적으로 제거된 아이템 리스트"
        )
    )


# ----
# (유니크 테스트 테이블 Row 수정 테스트)
class PutUniqueTestTableRowSampleInputVo(BaseModel):
    class Config:
        validate_by_name = True

    unique_value: int = (
        Field(
            ...,
            alias="uniqueValue",
            description="유니크 값",
            examples=[1]
        )
    )


class PutUniqueTestTableRowSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    uid: int = (
        Field(
            ...,
            alias="uid",
            description="글 고유번호",
            examples=[1]
        )
    )
    create_date: str = (
        Field(
            ...,
            alias="createDate",
            description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    update_date: str = (
        Field(
            ...,
            alias="updateDate",
            description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    unique_value: int = (
        Field(
            ...,
            alias="uniqueValue",
            description="유니크 값",
            examples=[1]
        )
    )


# ----
# (외래키 부모 테이블 Row 입력 API)
class PostFkParentRowSampleInputVo(BaseModel):
    class Config:
        validate_by_name = True

    fk_parent_name: str = (
        Field(
            ...,
            alias="fkParentName",
            description="외래키 테이블 부모 이름",
            examples=["홍길동"]
        )
    )


class PostFkParentRowSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    uid: int = (
        Field(
            ...,
            alias="uid",
            description="글 고유번호",
            examples=[1]
        )
    )
    create_date: str = (
        Field(
            ...,
            alias="createDate",
            description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    update_date: str = (
        Field(
            ...,
            alias="updateDate",
            description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    fk_parent_name: str = (
        Field(
            ...,
            alias="fkParentName",
            description="외래키 테이블 부모 이름",
            examples=["홍길동"]
        )
    )


# ----
# (외래키 부모 테이블 아래에 자식 테이블의 Row 입력 API)
class PostFkChildRowSampleInputVo(BaseModel):
    class Config:
        validate_by_name = True

    fk_child_name: str = (
        Field(
            ...,
            alias="fkChildName",
            description="외래키 테이블 자식 이름",
            examples=["홍길동"]
        )
    )


class PostFkChildRowSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    uid: int = (
        Field(
            ...,
            alias="uid",
            description="글 고유번호",
            examples=[1]
        )
    )
    create_date: str = (
        Field(
            ...,
            alias="createDate",
            description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    update_date: str = (
        Field(
            ...,
            alias="updateDate",
            description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
            examples=["2024_05_02_T_15_14_49_552_KST"]
        )
    )
    fk_parent_name: str = (
        Field(
            ...,
            alias="fkParentName",
            description="외래키 테이블 부모 이름",
            examples=["홍길동"]
        )
    )
    fk_child_name: str = (
        Field(
            ...,
            alias="fkChildName",
            description="외래키 테이블 자식 이름",
            examples=["홍길동"]
        )
    )


# ----
# (외래키 관련 테이블 Rows 조회 테스트)
class GetFkTestTableRowsSampleOutputVo(BaseModel):
    class Config:
        validate_by_name = True

    class ParentEntityVo(BaseModel):
        class Config:
            validate_by_name = True

        class ChildEntityVo(BaseModel):
            class Config:
                validate_by_name = True

            uid: int = (
                Field(
                    ...,
                    alias="uid",
                    description="글 고유번호",
                    examples=[1]
                )
            )
            create_date: str = (
                Field(
                    ...,
                    alias="createDate",
                    description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                    examples=["2024_05_02_T_15_14_49_552_KST"]
                )
            )
            update_date: str = (
                Field(
                    ...,
                    alias="updateDate",
                    description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                    examples=["2024_05_02_T_15_14_49_552_KST"]
                )
            )
            child_name: str = (
                Field(
                    ...,
                    alias="childName",
                    description="자식 테이블 이름",
                    examples=["test"]
                )
            )

        uid: int = (
            Field(
                ...,
                alias="uid",
                description="글 고유번호",
                examples=[1]
            )
        )
        create_date: str = (
            Field(
                ...,
                alias="createDate",
                description="글 작성일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        update_date: str = (
            Field(
                ...,
                alias="updateDate",
                description="글 수정일(yyyy_MM_dd_'T'_HH_mm_ss_SSS_z)",
                examples=["2024_05_02_T_15_14_49_552_KST"]
            )
        )
        parent_name: str = (
            Field(
                ...,
                alias="parentName",
                description="부모 테이블 이름",
                examples=["test"]
            )
        )
        child_entity_list: List[ChildEntityVo] = (
            Field(
                ...,
                alias="childEntityList",
                description="부모 테이블에 속하는 자식 테이블 리스트"
            )
        )

    parent_entity_vo_list: List[ParentEntityVo] = (
        Field(
            ...,
            alias="parentEntityVoList",
            description="부모 아이템 리스트"
        )
    )
