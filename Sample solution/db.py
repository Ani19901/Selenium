import pymssql  


class DB:

    #Create DB connection
    def create_connection(self):
        con = pymssql.connector.connect(server='sqllearn.volo.local',
                               user='pythonuser',
                               password='cA7BHCrLBEGh4CmZ',
                               database='AdventureWorks2019'
                               )
        return con


    def select_query(self, sql_query):
        try:
            #get connection
            db = self.create_connection()
            cursor = db.cursor()
            cursor.execute(sql_query)
            data = cursor.fetchone()
            return data

        except Exception as err:
            print(err)


    def insert_query(self, conn, sql_query):
        try:
            #get connection
            db = self.create_connection()
            cursor = db.cursor()
            cursor.execute(sql_query)
            conn.commit()
            return cursor.rowcount

        except Exception as err:
            print(err)


    def close_connection(self):
        self.create_connection().close()

