import psycopg2
from bd.database import session, Match


def is_online():
    try:
        session.query(Match).first()
    except psycopg2.OperationalError:
        return False
    else:
        return True


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








