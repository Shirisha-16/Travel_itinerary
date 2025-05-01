# app/seed.py
from app.database import Base, engine, SessionLocal
from app import models
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
db = SessionLocal()

phuket = models.TripItinerary(name="Phuket Adventure", nights=4, region="Phuket")
db.add(phuket)
db.commit()
db.refresh(phuket)

day1 = models.Day(day_number=1, trip_id=phuket.id)
db.add(day1)
db.commit()
db.refresh(day1)

db.add(models.Hotel(name="Sea Pearl Resort", day_id=day1.id))
db.add(models.Activity(name="Island Hopping", day_id=day1.id))
db.add(models.Transfer(description="Airport to Hotel", day_id=day1.id))

db.commit()
db.close()
