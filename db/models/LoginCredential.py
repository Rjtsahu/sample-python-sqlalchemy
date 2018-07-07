from sqlalchemy import Column, Integer, String, Sequence,ForeignKey
from sqlalchemy.orm import relationship,backref
from db import Base


class LoginCredential(Base):
    __tablename__ = 'login_credential'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(length=200))
    mobile = Column(String(length=10))
    password = Column(String(length=200))
    person_id = Column(Integer,ForeignKey('person.id'))
    person=relationship("Person",backref=backref("login_credential",uselist=False))

    def __repr__(self):
        return 'username: %s , mobile:%s , password:%s user:[%s]' % (self.username, self.mobile, self.password,self.person)
