from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain.Insurance import Insurance_router
from domain.Question import question_router
from domain.Answer import answer_router
from domain.User import user_router

app = FastAPI()

origins = [
    "https://youhave.store",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # 프론트엔드 접근 허가를 위한 CORS 설정
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(Insurance_router.router)
app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))


@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")