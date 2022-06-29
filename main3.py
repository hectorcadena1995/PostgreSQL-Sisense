import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='admin', host='localhost', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Fetching all the rows before the update
print("Contents of the Employee table: ")
sql = '''SELECT id, model, price
	FROM public.mobile;'''
cursor.execute(sql)
print(cursor.fetchall())

#Updating the records
sql = "select * from function"
cursor.execute(sql)
print("Table updated...... ")

#Fetching all the rows after the update
print("Contents of the Employee table after the update operation: ")
sql = '''SELECT id, model, price
	FROM public.mobile;'''
cursor.execute(sql)
print(cursor.fetchall())

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
