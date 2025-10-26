#!/usr/bin/python3
"""
Uses SQLAlchemy to extract objects matching the command line entry
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
        State.name.contains(sys.argv[4])).order_by(State.id).all()
    if state:
        print(f"{row.id}")
    else:
        print("Not found")

    session.close()
