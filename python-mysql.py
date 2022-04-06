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
cursor.execute("CREATE DATABASE my_database_name")

# commit the changes
conn.commit()
# to create a table
# cursor.execute("CREATE TABLE my_table_name(id INT, name VARCHAR(255))")

# commit the changes
# conn.commit()
# to insert data into a table
# cursor.execute("INSERT INTO my_table_name VALUES(1, 'John Reygun')")

# commit the changes
# conn.commit()
# to update data in a table
# cursor.execute("UPDATE my_table_name SET name = 'John Reygun Danag' WHERE id = 1")

# commit the changes
# conn.commit()
# to delete data in a table
# cursor.execute("DELETE FROM my_table_name WHERE id = 1")

# commit the changes
# conn.commit()
# to select data from a table
# cursor.execute("SELECT * FROM my_table_name")

# to fetch data from a table
# data = cursor.fetchall()
# print(data)

# to close the connection
conn.close()

# Code by: John Reygun Danag
