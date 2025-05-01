# Travel Itinerary Backend

A backend system built with FastAPI and SQLAlchemy to manage travel itineraries, including hotel stays, transfers, activities, and day-wise plans. Also includes a recommendation endpoint via an MCP server.

Features

- Create and view trip itineraries
- Day-wise hotel accommodations, transfers, and activities
- Recommended itineraries (MCP logic) based on number of nights
- Sample data seeded for Phuket and Krabi

 Tech Stack

- **FastAPI** – API framework
- **SQLAlchemy** – ORM for database modeling
- **SQLite** – Lightweight database
- **Pydantic** – Data validation

Getting Started

1. Clone the repository

In bash
git clone https://github.com/yourusername/travel-itinerary.git

cd travel-itinerary

2)Create Virtual Environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3)Install Dependencies

pip install -r requirements.txt

4)Run the server

uvicorn app.main:app --reload

5)Seed sample Data(optional)

python -m app.seed


