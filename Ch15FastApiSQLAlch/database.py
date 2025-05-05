import os
from dotenv import  load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

load_dotenv(dotenv_path='.env')

DATABASE_URL = os.getenv('DATABASE_URL')
engine=create_async_engine(DATABASE_URL,echo=True)
SessionLocal= async_sessionmaker(engine,expire_on_commit=False,class_=AsyncSession)