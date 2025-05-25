from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import create_short_url, get_short_url, validate_short_url
from database import get_db
from schemas import URLResponse, URLCreate
from utils import generate_short_url

router = APIRouter(prefix="/api", tags=["URL_API"])

@router.get(
    "/url_generate/{long_url}",
    summary="Short URL Generate",
    description="현재 시간과 난수를 결합한 값을 Base62로 인코딩하여 6~8자리의 고유한 short URL을 생성합니다.",
    response_description="생성된 Short URL 정보를 반환합니다.",
    response_model=URLResponse,
)
async def generate_url(long_url: str, db: AsyncSession = Depends(get_db)):
    print(f"generate_url() : Long URL : {long_url}")

    # Already exist long_url check
    url = await get_short_url(db, long_url)

    # url이 존재하면 이미 생성된 url 리턴
    if url:
        print(f"generate_url() : Already Exist URL : {url.short_url}")
        return url

    # Short URL
    short_url = await generate_unique_short_url(8, db)
    url_create = URLCreate(longUrl=long_url, shortUrl=short_url)
    created_url = await create_short_url(db, url_create)

    if not created_url:
        raise HTTPException(status_code=500, detail="Short URL Create Failed")

    print(f"generate_url() : Created URL : {created_url.short_url}")

    return created_url

# short_url 생성 후, 이미 중복되는 값이 존재하면, 다시 생성 후 중복되지 않을 때 까지 Return
async def generate_unique_short_url(length:int, db: AsyncSession):
    print(f"generate_unique_short_url() : Length : {length}")

    while True:
        result = generate_short_url(length=length)
        exists = await validate_short_url(db, result)
        if not exists:
            return result