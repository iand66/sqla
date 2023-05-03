from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ninum = Column("NINUM", Integer, primary_key=True)
    firstname = Column("Firstname", String)
    lastname = Column("Lastname", String)
    gender = Column("Gender", CHAR)
    age = Column("Age", Integer)

    def __init__(self, ninum, first, last, gender, age) -> None:
        self.ninum = ninum
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age
        
    def __repr__(self) -> str:
        return f"({self.ninum}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"

engine = create_engine("sqlite:///people.db", echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person1 = Person(12345, "Ian", "Davies", "M", 56)
person2 = Person(12346, "Jeanette", "Davies", "M", 59)

try:
    session.add(person1)
    session.add(person2)
    session.commit()
except IntegrityError as e:
    session.rollback()

results = session.query(Person).all()
print(results)

results = session.query(Person).filter(Person.lastname == 'Davies')
for r in results:
    print(r)
