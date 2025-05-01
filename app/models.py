from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class TripItinerary(Base):
    __tablename__ = "itineraries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    nights = Column(Integer)
    region = Column(String)

    days = relationship("Day", back_populates="trip")

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, index=True)
    day_number = Column(Integer)
    trip_id = Column(Integer, ForeignKey("itineraries.id"))

    trip = relationship("TripItinerary", back_populates="days")
    hotel = relationship("Hotel", uselist=False, back_populates="day")
    transfers = relationship("Transfer", back_populates="day")
    activities = relationship("Activity", back_populates="day")

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    day_id = Column(Integer, ForeignKey("days.id"))

    day = relationship("Day", back_populates="hotel")

class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    day_id = Column(Integer, ForeignKey("days.id"))

    day = relationship("Day", back_populates="transfers")

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    day_id = Column(Integer, ForeignKey("days.id"))

    day = relationship("Day", back_populates="activities")
