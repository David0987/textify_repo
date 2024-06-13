import pymysql

try:
    # Database connection parameters
    DB_HOST = 'myappdb.cnko8g4o2vn7.ap-southeast-1.rds.amazonaws.com'
    DB_PORT = 3306
    DB_NAME = 'myappdb'
    DB_USER = 'admin'
    DB_PASSWORD = 'myapp123'

    # Connect to the MySQL database
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME
    )

    print("Connected to the database successfully!")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Define the SQL statement to insert data into the table
    sql = "INSERT INTO records (column1, column2) VALUES (%s, %s)"

    # Define the records to insert
    records = [
        ('1', 'abc'),
        ('2', 'david rocks')
        # Add more records as needed
    ]

    # Execute the SQL statement for each record
    for record in records:
        cursor.execute(sql, record)

    # Commit the transaction
    connection.commit()

    print("Records inserted successfully!")

    # Don't forget to close the cursor and connection when you're done
    cursor.close()
    connection.close()

except pymysql.Error as e:
    print("Error connecting to the database:", e)



# import pymysql
#
# try:
#     # Database connection parameters
#     DB_HOST = 'myappdb.cnko8g4o2vn7.ap-southeast-1.rds.amazonaws.com'
#     DB_PORT = 3306
#     DB_NAME = 'myappdb'
#     DB_USER = 'admin'
#     DB_PASSWORD = 'myapp123'
#
#     # Connect to the MySQL database
#     connection = pymysql.connect(
#         host=DB_HOST,
#         port=DB_PORT,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         db=DB_NAME
#     )
#
#     print("Connected to the database successfully!")
#
#     # Don't forget to close the connection when you're done
#     connection.close()
#
# except pymysql.Error as e:
#     print("Error connecting to the database:", e)
