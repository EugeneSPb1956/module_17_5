from .db import SessionLocal

# функция-генератор для подключения к БД
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()