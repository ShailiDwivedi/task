import mysql.connector

def connect_to_mysql():
    try:
        # Establish a connection to the MySQL server
        host = 'localhost'
        username = 'root'
        password = 'root'
        database = 'Assignment'
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
        else:
            print("Failed to connect to MySQL database")
            return None
        
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

connect_to_mysql()

