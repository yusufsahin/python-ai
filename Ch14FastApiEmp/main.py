from fastapi import FastAPI
from contextlib import asynccontextmanager
from crud import create_table
from routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_table()  # Startup işlemleri
    yield
    # Shutdown işlemleri (örneğin: bağlantı kapatma) gerekirse buraya

app = FastAPI(title="Async Employee API", lifespan=lifespan)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
