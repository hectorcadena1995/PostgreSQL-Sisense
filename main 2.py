from unittest import result
import psycopg2

try:
    ps_connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    cursor = ps_connection.cursor()

    cursor.callproc('select * from function')

    ##postgreSQL_select_Query = "select * from public.mobile"

    ##cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    result = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in result:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if ps_connection:
        cursor.close()
        ps_connection.close()
        print("PostgreSQL connection is closed")