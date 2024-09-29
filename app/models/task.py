from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

# user_id - целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом.
    user = relationship('User', back_populates='tasks')
# user - объект связи с таблицей User, где back_populates='tasks'.
#     products = relationship("Product", back_populates="category")


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
