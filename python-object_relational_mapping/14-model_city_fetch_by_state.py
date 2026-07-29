#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Setup database connection engine using command line arguments
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Configure session context layout bound to connection engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query City and State together using an explicit relationship join
    # Sorted in ascending order by cities.id
    results = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id.asc()).all()

    # Loop through matched record entities and format display
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
