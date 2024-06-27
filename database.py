import mysql.connector as my_conn

def connect_to_mysql():
    try:
        # Establish a connection to the MySQL server
        host = 'localhost'
        username = 'root'
        password = '12345'
        database = 'Assignment'
        mydb = my_conn.connect(
            host= host,
            user= username,
            password= password,
            database= database
        )
        
        if mydb.is_connected():
            print("Connected to MySQL database")
            return mydb
        else:
            print("Failed to connect to MySQL database")
            return None
        
    except my_conn.Error as error:
        print("Error connecting to MySQL database:", error)
        return None
