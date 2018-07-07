from db import Base
from db import engine
from db import session
from datetime import datetime
# import all relevant db models here.
from db.models import Person


def create_database():
    print('creating database from given mappings')
    Base.metadata.create_all(engine)
    print('created mapping')


def create_test_record():
    person = Person.Person()
    person.name = 'test user 2'
    person.gender = False
    person.date_of_birth = datetime.utcnow()
    session.add(person)
    session.commit()
    session.close()
    print('data saved')


def fetch_all_person():
    persons = session.query(Person.Person).all()
    for person in persons:
        print(person)
