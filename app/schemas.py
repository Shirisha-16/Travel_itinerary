from pydantic import BaseModel
from typing import List, Optional

class Hotel(BaseModel):
    name: str
    class Config:
        orm_mode = True

class Transfer(BaseModel):
    description: str
    class Config:
        orm_mode = True

class Activity(BaseModel):
    name: str
    class Config:
        orm_mode = True

class Day(BaseModel):
    day_number: int
    hotel: Optional[Hotel]
    transfers: List[Transfer] = []
    activities: List[Activity] = []
    class Config:
        orm_mode = True

class TripItineraryCreate(BaseModel):
    name: str
    nights: int
    region: str
    days: List[Day]

class TripItinerary(TripItineraryCreate):
    id: int
    class Config:
        orm_mode = True
