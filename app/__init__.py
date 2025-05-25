import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from api import router
from database import create_tables

# create Tables의 Base.metadata 등록을 위해 import
import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("app start")

    # Setup Code =====
    await create_tables()
    print("Database Table Created !")

    yield

    print("app end")



def create_app() -> FastAPI:

    # 허용할 origin (프론트엔드 주소)
    origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

    app = FastAPI(
        lifespan=lifespan,
        title="shortURL",
        description="shortURL API",
        version="1.0.0",
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"]
            ),
        ]
    )

    #Router Include
    app.include_router(router)

    return app