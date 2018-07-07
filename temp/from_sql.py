# coding: utf-8
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Bu(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True)
    b_no = Column(Text)
    detail = Column(Text)


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    phone = Column(Integer)
    password = Column(Text)
    home_gps = Column(Text)
    token = Column(Text)
    expires = Column(Text)


class Journey(Base):
    __tablename__ = 'journey'

    id = Column(Integer, primary_key=True)
    j_type = Column(Boolean, server_default=text("1"))
    date = Column(Text)
    start = Column(Text, server_default=text("0"))
    end = Column(Text, server_default=text("0"))
    gps = Column(Text)
    b_id = Column(ForeignKey('bus.id'))
    last_update = Column(Text)

    b = relationship('Bu')


class Kid(Base):
    __tablename__ = 'kid'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    section = Column(Text)
    photo = Column(Text)
    p_id = Column(ForeignKey('parent.id'))
    b_id = Column(ForeignKey('bus.id'))

    b = relationship('Bu')
    p = relationship('Parent')


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    pick_present = Column(Boolean, server_default=text("0"))
    pick_gps = Column(Text)
    drop_gps = Column(Text)
    k_id = Column(ForeignKey('kid.id'))
    j_id = Column(ForeignKey('journey.id'))
    drop_present = Column(Boolean, server_default=text("0"))
    pick_time = Column(Text, server_default=text("0"))
    drop_time = Column(Text, server_default=text("0"))

    j = relationship('Journey')
    k = relationship('Kid')


class Driver(Base):
    __tablename__ = 'driver'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    userid = Column(Text)
    contact = Column(Integer)
    password = Column(Text)
    b_id = Column(ForeignKey('bus.id'))
    token = Column(Text)
    expires = Column(Text)
    active_ride_j_id = Column(ForeignKey('journey.id'), server_default=text("null"))

    active_ride_j = relationship('Journey')
    b = relationship('Bu')


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    gps = Column(Text)
    time = Column(Text)
    j_id = Column(ForeignKey('journey.id'))

    j = relationship('Journey')


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    title = Column(Text)
    message = Column(Text)
    date = Column(Text)
    p_id = Column(ForeignKey('parent.id'))
    d_id = Column(ForeignKey('driver.id'))

    d = relationship('Driver')
    p = relationship('Parent')
