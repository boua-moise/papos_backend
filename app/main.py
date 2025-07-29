from fastapi import FastAPI
from prisma import Prisma
from contextlib import asynccontextmanager
from app.routes.authentification import authentication
from app.routes.administration import admin_router
from app.routes.articles import article_router
from fastapi.middleware.cors import CORSMiddleware


prisma = Prisma(auto_register=True)

@asynccontextmanager
async def lifespan(app:FastAPI):
    await prisma.connect()
    yield
    if prisma.is_connected():
        await prisma.disconnect()

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["*"] temporairement
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication)
app.include_router(admin_router)
app.include_router(article_router)