from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True,index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    phone_number = Column(String,nullable=True)
    address = Column(String,nullable=True)