from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()


class User(Base):
    ''' Creates a table that stores a user's information '''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)


class Dream(Base):
    '''Creates a table that stores information about dream instances'''
    __tablename__ = 'Dream'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    story = Column(String(250), nullable=False)
    #Settings
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Location(Base):
    '''Creates a table with information about each location'''
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Dream_Instance(Base):
    '''Creates a table with information about a dream instance'''
    __tablename__ = 'dream_instance'

    id = Column(Integer, primary_key=True)
    time_start = Column(DateTime,
                        nullable=False,
                        default=datetime.datetime.utcnow)
    time_end = Column(DateTime, nullable=False, default=None)
    dream_id = Column(Integer, ForeignKey('dream.id'))
    dream = relationship(Dream)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship(Location)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Satisfaction(Base):
    '''Log of how satisfied users are with a particular dream instance'''
    __tablename__ = 'satisfaction'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime,
                        nullable=False,
                        default=datetime.datetime.utcnow)
    level = Column(Intenger, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    dream_instance_id = Column(Integer, ForeignKey('dream_instance.id'))
    dream_instance = relationship(Dream_Instance)


engine = create_engine('sqlite:///catalog_db.db')
Base.metadata.create_all(engine)
