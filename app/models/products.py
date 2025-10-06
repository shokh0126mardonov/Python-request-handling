from sqlalchemy import Column,String,Integer,Numeric,Text,ForeignKey
from ..db.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key = True,index=True)

    name = Column(String,nullable=False)
    descreption = Column(Text)
    price = Column(Numeric,nullable=False)

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer,primary_key = True,index=True)

    product_id = Column(Integer,ForeignKey('products.id',ondelete='CASCADE'),nullable=False)
    url = Column(String(length=256),nullable=False)
    