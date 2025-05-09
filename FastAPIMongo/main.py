from fastapi import FastAPI
from routes import router

app = FastAPI(title="Contact API (MongoDB)")

app.include_router(router)