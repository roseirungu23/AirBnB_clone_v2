#!/usr/bin/python3
"""Defines a class DBStorage"""

from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

class DBStorage:
    """Represents class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """initializes a DBStorage instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""

        classes = [State, City]

        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(session_factory)
    
    def close(self):
        """close the SQLALchemy"""
        self.__session.close()
