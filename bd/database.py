import psycopg2
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from VK_token import bd_user, bd_password

Base = declarative_base()
engine = sq.create_engine(f'postgresql://{bd_user}:{bd_password}@localhost:5432/vkinder')
Session = sessionmaker(bind=engine)

match = sq.Table(
    'match', Base.metadata,
    sq.Column('user_id', sq.Integer, sq.ForeignKey('user.id')),
    sq.Column('couple_id', sq.Integer, sq.ForeignKey('couple.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer)
    couple = relationship('Couple', secondary='match', back_populates='user', cascade='all,delete')


class Couple(Base):
    __tablename__ = 'couple'
    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer)
    user = relationship('User', secondary='match', back_populates='couple', cascade='all,delete')


session = Session()
# Base.metadata.create_all(engine)
couple1 = Couple(vk_id=1234)
couple2 = Couple(vk_id=11111)
user = User(vk_id=87878521)
user.couple.extend(couple1)
user.couple.append(couple2)


session.add(user)
session.commit()

