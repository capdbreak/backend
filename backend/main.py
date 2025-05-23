from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth_google import router as google_router
from app.routers.auth_register import router as register_router
from app.routers.stock_routes import router as stock_router
from app.routers import tickers
from app.routers.news import router as news_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:3000"],
    allow_origins=["http://34.22.108.245:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(google_router)
app.include_router(register_router)
app.include_router(stock_router)
app.include_router(tickers.router)
app.include_router(news_router)
