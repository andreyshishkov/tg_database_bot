from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from langchain_community.utilities import SQLDatabase

from app.config import db_password, db_user, database, db_host

db_uri = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:5432/{database}"
engine = create_async_engine(db_uri)
db = SQLDatabase.from_uri(db_uri.replace("+asyncpg", ""))

DATABASE_INFO = db.get_table_info()


async def perform_sql_query(sql_query: str):
    async with engine.connect() as conn:
        result = await conn.execute(text(sql_query))
        result = result.scalar()
    return result
