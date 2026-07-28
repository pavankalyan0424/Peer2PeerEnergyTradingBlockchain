# main.py


from fastapi import FastAPI
from app.api import health
from app.api import blockchain
from app.api import token
from app.api import marketplace

app = FastAPI(title="EnerChain Backend")

app.include_router(health.router)
app.include_router(blockchain.router)
app.include_router(token.router)
app.include_router(marketplace.router)
