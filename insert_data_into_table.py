from database import connect_to_mysql as conn
import mysql.connector
connection = conn()
mycursor = connection.cursor()

def insert_query(sql):
    try:
        mycursor.execute(sql)
        connection.commit()
    except mysql.connector.Error as error:
        print("Error inserting data:", error)
        connection.rollback()  # Rollback the transaction in case of an error.

# Example usage:
# SQL query to insert data
# sql_insert = "INSERT INTO your_table (column1, column2) VALUES ('value1', 'value2')"
# insert_query(sql_insert)


