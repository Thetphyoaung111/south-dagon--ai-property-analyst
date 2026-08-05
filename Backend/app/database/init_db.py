from app.database.database import engine, Base
from app.models.property import Property

Base.metadata.create_all(bind=engine)

print("Database created successfully!")