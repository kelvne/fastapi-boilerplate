from sqlmodel import Session, create_engine, select

from lib.config import DatabaseConfig

db_engine = create_engine(str(DatabaseConfig.POSTGRES_URI))
