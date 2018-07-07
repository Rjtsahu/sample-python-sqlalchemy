from db import Base
from db import engine
from db import session
from datetime import datetime
# import all relevant db models here.
from db.models.Person import Person
from db.models.LoginCredential import LoginCredential


def create_database():
    print('creating database from given mappings')
    Base.metadata.create_all(engine)
    print('created mapping')


def create_test_record():
    login = LoginCredential()
    login.username = 'testuser@gmail.com'
    login.mobile = '9696969696'
    login.password = 'test@123'

    person = Person()
    person.name = 'test with login'
    person.gender = True

    login.person = person
    session.add(login)
    session.commit()
    session.close()
    print('data saved')


def fetch_all_person():
    logins = session.query(LoginCredential).all()
    for login in logins:
        print(login)
