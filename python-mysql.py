# first learn the basics of python and mysql
# open your MYSQL server
# type pip install mysql-connector-python or mysql-connector in your terminal(cmd)
# then import mysql.connector
import mysql.connector

# to create a connection to your database server
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
)

# cursor to execute sql commands
cursor = conn.cursor()

# to create a database
cursor.execute("CREATE DATABASE this_is_my_database")

# commit the changes
conn.commit()
# to create a table
# cursor.execute("CREATE TABLE this_is_my_table(id INT, name VARCHAR(255))")

# commit the changes
# conn.commit()
# to insert data into a table
# cursor.execute("INSERT INTO this_is_my_table VALUES(1, 'John Reygun')")

# commit the changes
# conn.commit()
# to update data in a table
# cursor.execute("UPDATE this_is_my_table SET name = 'John Reygun Danag' WHERE id = 1")

# commit the changes
# conn.commit()
# to delete data in a table
# cursor.execute("DELETE FROM this_is_my_table WHERE id = 1")

# commit the changes
# conn.commit()
# to select data from a table
# cursor.execute("SELECT * FROM this_is_my_table")

# to fetch data from a table
# data = cursor.fetchall()
# print(data)

# to close the connection
conn.close()

# Code by: John Reygun Danag