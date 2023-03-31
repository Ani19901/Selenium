from Lesson10.db import DB


def test():

    insert_sql = "insert into dbo.Demo_AM(ID, Name) values (44, 'A')"
    dv_obj = DB()

    try:
        dv_obj.cursor()
        print("Connect DB")
        dv_obj.insert_sql(insert_sql)
        print("Insert the value to the DB")


    finally:
        dv_obj.close_database()
        print("Close DB")


if __name__ == '__main__':
    test()
