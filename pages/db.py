import mysql.connector

class Database:
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                         database='book_management_system',
                                         user='root',
                                         password='Prasad@421')
            print("DB started successfully ")
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as error:
            print("Failed to start MySQL: {}".format(error))


    def addNewAdmin(self, name, email, password, contact):
        try:
            
            query="INSERT INTO Admin ( name, email, password, contact) VALUES('"+ name +"', '"+email+"', '"+ password+"', '"+ contact+"')"
            self.cursor.execute(query)
            self.connection.commit()
            # cursor.execute("INSERT INTO Admin ( name, email, password, contact) VALUES(  '"+ name +"', '"+email+", "+ password+"', "+ contact+" )")
            print('User added successfully')
        except mysql.connector.Error as e:
            print("Failed to create a user: "+e.msg)

    def addNewUser(self, name, email, password, contact):
        try:
            
            query="INSERT INTO User ( name, email, password, contact) VALUES('"+ name +"', '"+email+"', '"+ password+"', '"+ contact+"')"
            self.cursor.execute(query)
            self.connection.commit()
            # cursor.execute("INSERT INTO Admin ( name, email, password, contact) VALUES(  '"+ name +"', '"+email+", "+ password+"', "+ contact+" )")
            print('User added successfully')
        except mysql.connector.Error as e:
            print("Failed to create a user: "+e.msg)

    def loginAdmin(self, userName, password):
        try:
            
            query="select * from Admin where email='"+userName+"' and password='"+password+"'"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data.count != 0:
                # print(data[0])
                return data
            else:
                print("User not existed!!")
            self.connection.commit()
            # cursor.execute("INSERT INTO Admin ( name, email, password, contact) VALUES(  '"+ name +"', '"+email+", "+ password+"', "+ contact+" )")
            print('User added successfully')
            return []
        except mysql.connector.Error as e:
            print("Failed to create a user: "+e.msg)
            return []
        
    
    def loginUser(self, userName, password):
        try:
            
            query="select * from User where email='"+userName+"' and password='"+password+"'"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data.count != 0:
                print(data)
                return data
            else:
                print("User not existed!!")
            self.connection.commit()
            # cursor.execute("INSERT INTO Admin ( name, email, password, contact) VALUES(  '"+ name +"', '"+email+", "+ password+"', "+ contact+" )")
            print('User added successfully')
            return [] 
        except mysql.connector.Error as e:
            print("Failed to create a user: "+e.msg)
            return []

    def checkAdminExists(self, userName):
        try:
            
            query="select * from Admin where email='"+userName+"'"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except mysql.connector.Error as e:
            print("Failed to create a user: "+e.msg)
            return []
    
    def checkUserExists(self, userName):
        try:
            
            query="select * from User where email='"+userName+"'"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except mysql.connector.Error as e:
            print("Failed to create a user: "+e.msg)
            return []


# db = Database()
# db.loginAdmin('a', 'b')
# db.addNewAdmin('mehu', 'mehu@hotmail.com', 'DipuLesbo', '6969696969')
