from app.database.database import SessionLocal
from app.models.property import Property
from app.services.csv_import import load_dataset


def import_to_database():
    db = SessionLocal()

    df = load_dataset()

    for _, row in df.iterrows():
        property_item = Property(
            township=row["township"],
            ward=row["ward"],
            land_size=f'{row["land_width_ft"]}x{row["land_length_ft"]}',
            document_type=row["document_type"],
            price=row["asking_price_lakh"],
            road=row["road_type"],
            phone=row["phone"],
        )

        db.add(property_item)

    db.commit()
    db.close()

    print(f"Imported {len(df)} properties successfully.")


if __name__ == "__main__":
    import_to_database()