import psycopg2
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Settings import bd_user, bd_password, DB_name


Base = declarative_base()
engine = sq.create_engine(f'postgresql://{bd_user}:{bd_password}@localhost:5432/{DB_name}')
Session = sessionmaker(bind=engine)


class Match(Base):
    __tablename__ = 'match'
    user_id = sq.Column(sq.Integer, primary_key=True)
    couple_id = sq.Column(sq.Integer, primary_key=True)
    primary_key = True


session = Session()
Base.metadata.create_all(engine)


