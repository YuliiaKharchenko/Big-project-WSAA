# Activities DAO
# A data layer that connects to a database


import mysql.connector
import dbconfig as cfg
class ActivitiesDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def close_all(self):
        self.connection.close()
        self.cursor.close()
         
    def get_all(self):
        cursor = self.getcursor()
        sql="select * from activities"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convert_to_dictionary(result))
        
        self.close_all()
        return returnArray

    def find_by_number(self, number):
        cursor = self.getcursor()
        sql="select * from activities where number = %s"
        values = (number,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convert_to_dictionary(result)
        self.close_all()
        return returnvalue

    def create(self, activities):
        cursor = self.getcursor()
        sql="insert into activities (number, category, name, duration) values (%s,%s,%s,%s)"
        values = (activities.get("number"), activities.get("category"), activities.get("name"), activities.get("duration"))
        cursor.execute(sql, values)

        self.connection.commit()
        new_number = cursor.lastrowid
        activities["number"] = new_number
        self.close_all()
        return activities


    def update(self, number, activities):
        cursor = self.getcursor()
        sql="update  activities set category = %s, name = %s, duration = %s  where number = %s"
        
        values = (activities.get("category"), activities.get("name"), activities.get("duration"), number)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()
        
    def delete(self, number):
        cursor = self.getcursor()
        sql="delete from activities where number = %s"
        values = (number,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.close_all()
        
        print("Delete is done!")

    def convert_to_dictionary(self, resultLine):
        attkeys=["number","category","name", "duration"]
        activities = {}
        currentkey = 0
        for attrib in resultLine:
            activities[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return activities 

        
activitiesDAO = ActivitiesDAO()