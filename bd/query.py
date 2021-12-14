import psycopg2
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from VK_token import bd_user, bd_password
from bd.database import session, Match


def is_in_db(user_id, couple_id):
    result = session.query(Match).filter(Match.user_id == user_id).filter(Match.couple_id == couple_id).all()
    if len(result) == 0:
        return False
    else:
        return True


def add_in_db(user_id, couple_id):
    match = Match(user_id=user_id, couple_id=couple_id)
    session.add(match)
    session.commit()








