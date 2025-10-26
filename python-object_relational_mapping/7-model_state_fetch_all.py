#!/usr/bin/python3
"""
Uses SQLAlchemy to access and list data from model_state
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
        f"mysql+pymysql://{username}:{passwd}@localhost:3306/{db_name}"
        )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()
    for row in result:
        print(f"{row.id}: {row.name}")
