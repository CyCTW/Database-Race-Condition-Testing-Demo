from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URI = 'postgresql://cyctw:1234@localhost:5432/cyctw'
POSTGRES_USER="unicorn_user"
POSTGRES_PASS="magical_password"
POSTGRES_HOST="postgres-db"
POSTGRES_DBNAME="postgres"

SQLALCHEMY_DATABASE_URI = f"postgresql://\
{POSTGRES_USER}:{POSTGRES_PASS}@\
{POSTGRES_HOST}:5432/{POSTGRES_DBNAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
