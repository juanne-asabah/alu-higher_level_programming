#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve arguments passed via command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Execute the SQL query filtering for states starting with 'N'
    # BINARY ensures case-sensitivity to strictly catch upper-case N
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch all the rows returned by the query
    query_rows = cursor.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Clean up and close connections
    cursor.close()
    db.close()
