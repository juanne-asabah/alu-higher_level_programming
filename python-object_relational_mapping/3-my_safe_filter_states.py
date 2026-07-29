#!/usr/bin/python3
"""
Displays all values in the states table matching the user input argument.
Safeguarded against malicious SQL Injection using parameterized queries.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve arguments passed via command line
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

    # Use a parameterized query (%s) to prevent SQL Injection safely
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch all matching rows
    query_rows = cursor.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Clean up and close connections
    cursor.close()
    db.close()
