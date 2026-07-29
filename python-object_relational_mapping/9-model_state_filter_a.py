#!/usr/bin/python3
"""
Lists all State objects containing the letter 'a' from database hbtn_0e_6_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
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

    # Query State objects containing 'a' sorted by id in ascending order
    states_with_a = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id.asc()).all()

    # Display results exactly as shown in the example output structure
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
