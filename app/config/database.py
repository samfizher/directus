from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://root:root@db:5432/directus_db"
SQLALCHEMY_DATABASE_URL = "postgresql://vchhqldyvtwswc:59c5ddb2fddb61356974baa49f41255e397295e069ede271c528dfa3c6968844@ec2-63-32-230-6.eu-west-1.compute.amazonaws.com:5432/dfrdhpra79aclc"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)
