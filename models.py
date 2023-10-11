from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(25), unique=True)
    password = Column(String(25), nullable=True)
    

class Item(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('Users.id'))