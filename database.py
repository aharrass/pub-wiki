from contextlib import asynccontextmanager

from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import settings

# 비동기 엔진 생성
engine = create_async_engine(settings.DB_URL, echo=True)


# 세션 팩토리 생성
AsyncSession = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class
Base = declarative_base()

# Context for Async Database
@asynccontextmanager
async def get_async_session() -> AsyncSession:

    async with AsyncSession() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e

# Depend Session DB Function
async def get_db() -> AsyncSession:
    try:
        async with AsyncSession() as session:
            yield session
    except OperationalError as oError:
        print(f'get_db() : Database Connect Failed : {oError}')
    except Exception as e:
        print(f'get_db() : Occurs Error : {e}')
        raise e

# Models All Table Create
async def create_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        print(f'Occurs Error during Create Table Trying : {e}')
        raise e