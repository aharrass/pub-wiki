1. python libraries

> 1. pydantic
> 2. pydantic_settings
> 3. sqlalchemy
> 4. asyncio
> 5. asnycpg
> 

2. Database
> short_url
> 
> ID : postgres
> 
> PW : test123!@#


3. File Architecture
```
shortURL/
└── app/
    ├── __init__.py     # 패키지 초기화 파일
    └── main.py         # FastAPI 진입점 (app 인스턴스 생성 및 실행)
├── api.py              # API 라우터 정의
├── config.py           # 설정 및 환경 변수 관리
├── crud.py             # DB에 대한 CRUD 로직 정의
├── database.py         # DB 연결 및 세션 관리
├── models.py           # SQLAlchemy ORM 모델 정의
├── schemas.py          # Pydantic 데이터 검증 모델 정의
├── utils.py            # 유틸리티 함수들 (Base62 인코딩 등)
├── shortURL.iml        # IntelliJ 프로젝트 설정 파일
├── test_main.http      # HTTP 요청 테스트 파일
├── .env                # 환경 변수 파일
├── .gitignore          # Git 제외 파일 목록
└── Readme.md           # 프로젝트 설명 문서
```