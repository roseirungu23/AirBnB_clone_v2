#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import Foreignkey
from sqlalchemy import String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Inherits from BaseModel and Base """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),ForeignKey("staetes.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
