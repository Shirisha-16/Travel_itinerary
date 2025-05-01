from sqlalchemy.orm import Session
from . import models, schemas

def create_itinerary(db: Session, itinerary: schemas.TripItineraryCreate):
    db_itinerary = models.TripItinerary(name=itinerary.name, nights=itinerary.nights, region=itinerary.region)
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)

    for day_data in itinerary.days:
        db_day = models.Day(day_number=day_data.day_number, trip_id=db_itinerary.id)
        db.add(db_day)
        db.commit()
        db.refresh(db_day)

        if day_data.hotel:
            db_hotel = models.Hotel(name=day_data.hotel.name, day_id=db_day.id)
            db.add(db_hotel)

        for transfer in day_data.transfers:
            db.add(models.Transfer(description=transfer.description, day_id=db_day.id))

        for activity in day_data.activities:
            db.add(models.Activity(name=activity.name, day_id=db_day.id))

    db.commit()
    return db_itinerary

def get_itineraries(db: Session):
    return db.query(models.TripItinerary).all()
