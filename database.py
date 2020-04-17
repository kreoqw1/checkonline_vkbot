import pymysql.cursors 

def getconnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='your_password',                             
                                 db='checkonline',
                                 charset='utf8mb4',  
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def getquery(query):
    connection = getconnection()
        
    with connection.cursor() as cursor:
        print(query)
        cursor.execute(query)
        for row in cursor:
            connection.close()
            return row
    

def setquery(query):
    connection = getconnection()
                                     
    with connection.cursor() as cursor:
        print(query)
        cursor.execute(query)
        connection.commit()
    connection.close()

