import pandas as pd
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.property import Property

EXCEL_FILE = "../Datasets/properties.xlsx"


def import_data():
    df = pd.read_excel(EXCEL_FILE)

    db: Session = SessionLocal()

    for _, row in df.iterrows():
        property_item = Property(
            township=row["township"],
            ward=row["ward"],
            land_size=row["land_size"],
            document_type=row["document_type"],
            price=row["price"],
            road=row.get("road"),
            phone=row.get("phone"),
        )
        db.add(property_item)

    db.commit()
    db.close()

    print("Import completed successfully!")


if name == "__main__":
    import_data()