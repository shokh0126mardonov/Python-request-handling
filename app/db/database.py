from sqlalchemy import URL,create_engine
from sqlalchemy.orm import declarative_base

from ..config import settings

url_object = URL.create(
    drivername = 'postgresql+psycopg2',
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    port=settings.DB_PORT,
    host=settings.DB_HOST,
    database=settings.DB_NAME
)

engine = create_engine(url_object)

Base = declarative_base() 