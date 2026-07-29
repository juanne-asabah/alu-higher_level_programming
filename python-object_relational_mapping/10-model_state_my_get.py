#!/usr/bin/python3
"""
Prints the State object id with the name passed as an argument.
Takes 4 arguments: mysql username, password, database, and state name.
Safe from SQL injection.
"""
import sys
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

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Capture the 4th argument containing the search string
    state_name_searched = sys.argv[4]

    # Query matching state name using a safe column comparison filter
    state = session.query(State).filter(
        State.name == state_name_searched
    ).first()

    # Display only the numeric ID if found, otherwise print Not found
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close session
    session.close()
