from fastapi import FastAPI

from dotenv import load_dotenv

from routers import base

load_dotenv()


app = FastAPI()

app.include_router(base.base_router)

