#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # Instantiate the new State object instance
    new_state = State(name="Louisiana")

    # Stage the object and commit it to the database table persistent layer
    session.add(new_state)
    session.commit()

    # Print the newly generated states.id value
    print("{}".format(new_state.id))

    # Close session
    session.close()
