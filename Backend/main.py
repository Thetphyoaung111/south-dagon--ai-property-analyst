from fastapi import FastAPI

from app.database.database import SessionLocal
from app.models.property import Property

app = FastAPI(
    title="South Dagon AI Property Analyst",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "South Dagon AI Property Analyst is running successfully!"
    }


@app.get("/properties")
def get_properties():
    db = SessionLocal()

    properties = db.query(Property).all()

    result = []

    for p in properties:
        result.append({
            "id": p.id,
            "township": p.township,
            "ward": p.ward,
            "land_size": p.land_size,
            "document_type": p.document_type,
            "price": p.price,
            "road": p.road,
            "phone": p.phone
        })

    db.close()

    return result