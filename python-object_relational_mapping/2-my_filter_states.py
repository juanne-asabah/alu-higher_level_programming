#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Takes 4 arguments: username, password, database name, and state name to search.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve all 4 arguments passed via command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL database server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Formulate the query using string format as strictly instructed
    # BINARY ensures case-sensitive exact matching
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name_searched)
    cursor.execute(query)

    # Fetch all matching rows
    query_rows = cursor.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Clean up and close connections
    cursor.close()
    db.close()
