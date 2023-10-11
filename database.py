from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
from sqlalchemy_utils import database_exists, create_database
from models import Base

engine = create_engine(
    f'postgresql://{dotenv_values(".env")["POSTGRES_USERNAME"]}:{dotenv_values(".env")["POSTGRES_PASSWORD"]}@localhost/users_and_items',
    echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
