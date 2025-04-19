# controllers/user_controller.py
from fastapi import APIRouter
from fastapi import FastAPI, Query, Response
from typing import Optional, List
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/user",  # 전체 경로 앞에 붙는 prefix
    tags=["User API"]  # Swagger 문서에서 구분되는 그룹 이름
)


class GetRequestTestOutputVo(BaseModel):
    queryParamString: str = Field(..., description="입력한 String Query 파라미터", example="testString")
    queryParamStringNullable: Optional[str] = Field(None, description="입력한 String Nullable Query 파라미터",
                                                    example="testString")
    queryParamInt: int = Field(..., description="입력한 Int Query 파라미터", example=1)
    queryParamIntNullable: Optional[int] = Field(None, description="입력한 Int Nullable Query 파라미터", example=1)
    queryParamDouble: float = Field(..., description="입력한 Double Query 파라미터", example=1.1)
    queryParamDoubleNullable: Optional[float] = Field(None, description="입력한 Double Nullable Query 파라미터", example=1.1)
    queryParamBoolean: bool = Field(..., description="입력한 Boolean Query 파라미터", example=True)
    queryParamBooleanNullable: Optional[bool] = Field(None, description="입력한 Boolean Nullable Query 파라미터", example=True)
    queryParamStringList: List[str] = Field(..., description="입력한 StringList Query 파라미터",
                                            example=["testString1", "testString2"])
    queryParamStringListNullable: Optional[List[str]] = Field(None, description="입력한 StringList Nullable Query 파라미터",
                                                              example=["testString1", "testString2"])


@router.get("/get-request", response_model=GetRequestTestOutputVo, summary="Get 요청 테스트 (Query Parameter)",
            description="Query Parameter 를 받는 Get 메소드 요청 테스트")
def get_request_test(
        response: Response,
        queryParamString: str = Query(..., description="String Query 파라미터", example="testString"),
        queryParamStringNullable: Optional[str] = Query(None, description="String Query 파라미터 Nullable",
                                                        example="testString"),
        queryParamInt: int = Query(..., description="Int Query 파라미터", example=1),
        queryParamIntNullable: Optional[int] = Query(None, description="Int Query 파라미터 Nullable", example=1),
        queryParamDouble: float = Query(..., description="Double Query 파라미터", example=1.1),
        queryParamDoubleNullable: Optional[float] = Query(None, description="Double Query 파라미터 Nullable", example=1.1),
        queryParamBoolean: bool = Query(..., description="Boolean Query 파라미터", example=True),
        queryParamBooleanNullable: Optional[bool] = Query(None, description="Boolean Query 파라미터 Nullable",
                                                          example=True),
        queryParamStringList: List[str] = Query(..., description="StringList Query 파라미터",
                                                example=["testString1", "testString2"]),
        queryParamStringListNullable: Optional[List[str]] = Query(None, description="StringList Query 파라미터 Nullable",
                                                                  example=["testString1", "testString2"])
):
    return GetRequestTestOutputVo(
        queryParamString=queryParamString,
        queryParamStringNullable=queryParamStringNullable,
        queryParamInt=queryParamInt,
        queryParamIntNullable=queryParamIntNullable,
        queryParamDouble=queryParamDouble,
        queryParamDoubleNullable=queryParamDoubleNullable,
        queryParamBoolean=queryParamBoolean,
        queryParamBooleanNullable=queryParamBooleanNullable,
        queryParamStringList=queryParamStringList,
        queryParamStringListNullable=queryParamStringListNullable
    )
