from db import DB


select_query = ""
insert_query = ""

#create object and call function
test_conn = DB()
test_conn.insert_query(insert_query)
test_conn.select_query(select_query)
test_conn.close_connection()





