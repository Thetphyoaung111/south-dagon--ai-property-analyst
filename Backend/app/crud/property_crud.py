from sqlalchemy.orm import Session

from app.models.property import Property


def create_property(db: Session, property_data: dict):
    property_item = Property(**property_data)

    db.add(property_item)
    db.commit()
    db.refresh(property_item)

    return property_item


def get_all_properties(db: Session):
    return db.query(Property).all()