#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Takes 4 arguments: mysql username, password, database, and state name.
Safe from SQL injection.
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

    # Join tables and use %s placeholder to prevent SQL injection
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (state_name_searched,))

    # Fetch all matching rows
    query_rows = cursor.fetchall()

    # Format output as a clean comma-separated line matching assignment style
    cities_list = [row[0] for row in query_rows]
    print(", ".join(cities_list))

    # Clean up and close connections
    cursor.close()
    db.close()
