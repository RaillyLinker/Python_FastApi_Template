from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from contextlib import asynccontextmanager
from functools import wraps
from zoneinfo import ZoneInfo
from sqlalchemy.orm import declarative_base

# DB 유저 인증 정보
_user_name = "root"
_password = "todo1234!"

# DB 타임존 설정
db_timezone = ZoneInfo("Asia/Seoul")

# db entity Base 객체
Base = declarative_base()

# 비동기 MySQL URL
_database_url = (
    f"mysql+asyncmy://{_user_name}:{_password}@127.0.0.1:3306/first_schema?"
    f"charset=utf8mb4"
)

# 엔진
_async_engine = (
    create_async_engine(
        _database_url,
        echo=False,  # DB 로그
        # 커넥션 풀에서 커넥션을 꺼내기 전에, SELECT 1 같은 간단한 쿼리를 보내 유효성 검사를 함.
        # 커넥션이 죽어 있다면 → 버리고 새로 연결.
        # 결과적으로, "OperationalError: MySQL server has gone away", "connection closed" 같은 에러를 방지할 수 있음.
        pool_pre_ping=True,
        pool_recycle=1800,  # 30분마다 커넥션 재생성
        pool_size=20,  # 커넥션 풀 크기
        max_overflow=10,  # 커넥션 풀을 넘어서 생성할 수 있는 커넥션 수
        pool_timeout=30,  # 커넥션 풀에서 대기할 최대 시간
    )
)

# 세션 메이커
_async_session_maker = (
    async_sessionmaker(
        bind=_async_engine,
        expire_on_commit=False,
        autoflush=False
    )
)


# (DB 세션을 반환하는 함수)
@asynccontextmanager
async def get_async_db() -> AsyncSession:
    async with _async_session_maker() as session:
        yield session


# (Transactional 데코레이터)
# Transaction 을 적용 하려는 함수 위에,
# @sql_alchemy_transactional(view_only=True) 이렇게 붙이고, 해당 함수에는,
# db: AsyncSession 이것을 인자값으로 받도록 처리
def sql_alchemy_transactional(view_only: bool = False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with get_async_db() as db:
                if view_only:
                    result = await func(*args, db=db, **kwargs)
                    return result
                else:
                    try:
                        result = await func(*args, db=db, **kwargs)
                        await db.commit()
                        return result
                    except Exception as e:
                        await db.rollback()
                        raise e

        return wrapper

    return decorator
