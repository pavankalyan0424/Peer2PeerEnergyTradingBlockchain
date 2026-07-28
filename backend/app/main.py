# main.py


from fastapi import FastAPI
from app.api import health

app = FastAPI(title="EnerChain Backend")

app.include_router(health.router)
