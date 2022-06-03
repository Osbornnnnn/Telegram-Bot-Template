from app import config
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(config.DATABASE_URI)
base = declarative_base()
base.metadata.bind = engine
base.metadata.create_all(engine)

@contextmanager
def db_session():
    session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
