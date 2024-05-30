from database import connect_to_mysql as conn

connection = conn()
mycursor = connection.cursor()

def check_data(sql):
    mycursor.execute(sql)
    tables = mycursor.fetchall()
    return tables

