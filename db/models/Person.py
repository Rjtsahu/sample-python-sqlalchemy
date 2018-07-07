from sqlalchemy import Column, Integer, String, Boolean, Sequence
from db import Base


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(length=200))
    date_of_birth = Column(String, name='dob')

    gender = Column(Boolean(), default=True)

    def __repr__(self):
        return 'name: %s , dob:%s , gender:%s' % (self.name, self.date_of_birth, self.gender)
