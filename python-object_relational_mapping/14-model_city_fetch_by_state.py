#!/usr/bin/python3
"""
Uses SQLAlchemy to access and list data from model_state
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
        )

#    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")
