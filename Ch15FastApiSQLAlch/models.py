from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"

    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    full_name:Mapped[str]=mapped_column(String(100))
    email:Mapped[str]=mapped_column(String(100), unique=True)
    phone:Mapped[str]=mapped_column(String(20))