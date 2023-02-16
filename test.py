import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='book_management_system',
                                         user='root',
                                         password='Prasad@421')
    print("Laptop Table created successfully ")
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))