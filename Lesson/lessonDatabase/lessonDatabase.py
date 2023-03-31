import pymssql

conn = pymssql.connect(server='sqllearn.volo.local',
                       user='pythonuser',
                       password='cA7BHCrLBEGh4CmZ',
                       database='AdventureWorks2019')

try:
    cursor = conn.cursor()
    insert_sql = "insert into dbo.Demo_AM(ID, Name) values (10, 'new_data')"
    cursor.execute(insert_sql)
    conn.commit()
    print('bla')


    cursor = conn.cursor()

    update_sql = "update dbo.Demo_AM set Name='Automation_3'"
    cursor.execute(update_sql)
    conn.commit()

    print('bla')
    print(cursor.rowcount)

    select_sql = "select * from dbo.Demo_AM where ID = 100"
    cursor.execute(select_sql)
    print("bla, bla")

    select_sql = "select * from dbo.Demo_AM"
    cursor.execute(select_sql)
    print(cursor.fetchone())

    rows = cursor.fetchall()
    for i in rows:
        print(i)
    conn.close()
    print('bla, bla')

except Exception as e:
    print(e)
    conn.rollback()