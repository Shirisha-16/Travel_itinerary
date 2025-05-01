from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from typing import List
from app.database import engine, SessionLocal, Base
from app.mcp_server import get_recommended_itinerary





Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/recommendation/")
def recommend_itinerary(nights: int, db: Session = Depends(get_db)):
    itinerary = get_recommended_itinerary(db, nights)
    if itinerary is None:
        raise HTTPException(status_code=404, detail="No itinerary found")
    return itinerary

@app.post("/itineraries/", response_model=schemas.TripItinerary)
def create_itinerary(itinerary: schemas.TripItineraryCreate, db: Session = Depends(get_db)):
    return crud.create_itinerary(db, itinerary)

@app.get("/itineraries/", response_model=List[schemas.TripItinerary])
def read_itineraries(db: Session = Depends(get_db)):
    return crud.get_itineraries(db)
