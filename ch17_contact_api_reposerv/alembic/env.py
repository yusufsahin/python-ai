from logging.config import fileConfig
import asyncio
import os
import sys
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context

# FastAPI app klasörüne erişmek için path ayarı
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.db.base import Base  # SQLAlchemy Base
from app.core.config import settings  # .env üzerinden config

# Alembic Config
config = context.config

# .env'deki DATABASE_URL'i alembic config'e yaz
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# SQLAlchemy Metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Offline migration (engine yok)"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Migration işlemlerini çalıştır"""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  # Tip değişikliklerini algıla
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Online migration (async engine kullanır)"""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
