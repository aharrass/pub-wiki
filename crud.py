from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from models import URL
from schemas import URLCreate


# Create Short URL
async def create_short_url(db : AsyncSession, url_create: URLCreate) -> Optional[URL]:
    """
    url_create 정보를 토대로 short_url row 생성
    :param db: Database Session
    :param url_create: URL Create Instance
    :return: URL Instance
    """

    try:
        url = URL(**url_create.model_dump(exclude_unset=True))
        print(f"Create URL : {url_create.short_url}, {url_create.long_url}")

        db.add(url)
        await db.commit()
        await db.refresh(url)

        return url
    except SQLAlchemyError as e:
        print(f'create_short_url() : Occurs Error : {e}')
        raise e

# Search Long URL
async def get_short_url(db : AsyncSession, long_url: str) -> Optional[URL]:
    """
    long_url정보를 토대로 기존에 존재하는 short_url이 있는 지 확인
    :param db: Database Session
    :param long_url: Long URL
    :return: URL Instance
    """
    result = await db.execute(
        select(URL).where(URL.long_url == long_url)
    )

    url = result.scalar_one_or_none()

    # if not url:
    #     raise HTTPException(status_code=404, detail=f"Not found URL - {long_url}")

    return url
