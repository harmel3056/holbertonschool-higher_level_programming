#!/usr/bin/python3
"""
Uses SQLAlchemy to extract a list of objects in model_state containing 'a'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for row in state:
        print(f"{row.id}: {row.name}")

session.close()
