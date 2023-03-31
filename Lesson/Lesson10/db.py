import pymssql

class DB:

    def __init__(self):
        self.conn = pymssql.connect(server='sqllearn.volo.local',
                           user='pythonuser',
                           password='cA7BHCrLBEGh4CmZ',
                           database='AdventureWorks2019')


    def cursor(self):
        cursor = self.conn.cursor()
        return cursor


    def insert_sql(self,insert_sql):
        self.cursor().execute(insert_sql)
        self.conn.commit()


    def close_database(self):
        self.cursor().close()




