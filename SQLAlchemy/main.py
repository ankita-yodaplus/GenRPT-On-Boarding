from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/satutorialdatabase',echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    things = relationship("Thing", back_populates="person")

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    price = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))
    person = relationship("Person", back_populates="things")



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Thing.owner, func.sum(Thing.price)).group_by(Thing.owner).having(func.sum(Thing.price) > 200).all()
print(result)

session.commit()

# result = session.query(Person).filter(Person.name == "Charlie").update({"name":"Charles"})
# session.commit()

# result = session.query(Person.name, Thing.description).join(Thing).all()
# print(result)

# result = session.query(Thing).filter(Thing.price < 50).delete()
# session.commit()
# result = session.query(Thing).filter(Thing.price < 50).all()
# print([t.description for t in result])


# result = session.query(Person).filter(Person.age>50).all()
# print([p.name for p in result])

# result = session.query(Person.name,Person.age).all()
# print(result)

# new_person = Person(name="Charlie", age=70)
# session.add(new_person)
# session.flush()

# new_thing = Thing(description="smartwatch", price=200.00, owner=new_person.id)
# session.add(new_thing)
# session.commit()

# print([t.description for t in new_person.things])
# print(new_thing.person.name)