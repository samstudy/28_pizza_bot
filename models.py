from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

URI = os.environ['DATABASE_URL']
engine = create_engine(URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    options = relationship("Option", back_populates="pizza")

    def __repr__(self):
        return "title='%s', description='%s'" % (self.title, self.description)


class Option(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True)
    size = Column(String)
    price = Column(Integer)
    pizza_id = Column(Integer, ForeignKey('pizza.id'))
    pizza = relationship("Pizza", back_populates="options")

    def __repr__(self):
        return "size='%s', price='%s'" % (self.size, self.price)
