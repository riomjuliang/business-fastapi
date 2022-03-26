from src.database import Base, engine, SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
