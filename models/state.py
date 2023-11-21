#!/usr/bin/python3
""" Defines State class """
from os import getenv
import models
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base

class State(BaseModel, Base):
    """ State class for a MySQL database"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Gets list of all cities objects related to state_id"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
