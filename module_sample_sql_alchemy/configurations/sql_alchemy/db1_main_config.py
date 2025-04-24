from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# DB 유저 인증 정보
user_name = "root"
password = "todo1234!"

# 비동기 MySQL URL
database_url = (
    f"mysql+asyncmy://{user_name}:{password}@127.0.0.1:3306/first_schema?"
    f"charset=utf8mb4"
)

# 엔진
async_engine = (
    create_async_engine(
        database_url,
        echo=True,
        pool_pre_ping=True
    )
)

# 세션 메이커
AsyncSessionLocal = (
    async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False
    )
)


# 의존성 주입용 세션 함수
@asynccontextmanager
async def get_async_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
