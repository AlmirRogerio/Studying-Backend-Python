import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from tortoise import Tortoise

from router import api_router

app = FastAPI()
app.include_router(router=api_router)
load_dotenv("./.env")

@app.on_event("startup")
async def startup():
    await Tortoise.init(
        db_url=os.environ.get("MY_DATABASE", ""),
        modules={"models": ["models.models"]},
    )
    
    await Tortoise.generate_schemas()
