from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bill_cast.core.config import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
