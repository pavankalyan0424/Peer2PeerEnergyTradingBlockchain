# main.py


from fastapi import FastAPI
from app.api import health
from app.api import blockchain
from app.api import token
from app.api import marketplace
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="EnerChain Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(blockchain.router)
app.include_router(token.router)
app.include_router(marketplace.router)
