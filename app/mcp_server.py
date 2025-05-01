from sqlalchemy.orm import Session
from .models import TripItinerary

def get_recommended_itinerary(db: Session, nights: int):
    return db.query(TripItinerary).filter(TripItinerary.nights == nights).first()
