from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud import create_short_url, get_short_url
from database import get_db
from schemas import URLResponse, URLCreate
from utils import generate_short_url

router = APIRouter(prefix="/api", tags=["URL_API"])

@router.get("/url_generate/{long_url}", response_model=URLResponse)
async def generate_url(long_url: str, db: AsyncSession = Depends(get_db)):

    # Already exist long_url check
    url = await get_short_url(db, long_url)

    # 이미 존재하는 short_url이 없으면
    if not url:
        # Short URL
        short_url = generate_short_url(8)
        url_create = URLCreate(longUrl=long_url, shortUrl=short_url)
        return await create_short_url(db, url_create)
    else:
        return url