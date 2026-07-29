#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
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

    # Bind engine metadata definitions
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Instantiate a live database session context block
    session = Session()

    # Query all State objects sorted in ascending order by id
    states = session.query(State).order_by(State.id.asc()).all()

    # Iterate and display results matching the required format structure
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
