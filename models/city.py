#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import Foreignkey
from sqlalchemy import String


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60),ForeignKey("staetes.id"), nullable=False)
    name = Column(String(128), nullable=False)
