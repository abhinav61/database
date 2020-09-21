import mysql.connector
from mysql.connector import Error

name = input("Enter the database name: ")
username = input("Enter the user name: ")
passwd = input("Enter the password: ")
mydb = mysql.connector.connect(
    host ="localhost",
    user=f"{username}",
    passwd=f"{passwd}",
    database=f"{name}",
)
print(mydb)

my_cursor = mydb.cursor()

def insert_key():
    table_name = input("Enter the name of the table: ")
    if table_name == "customers":
        table = input("Enter the table name: ")
        first = input("Enter the first name: ")
        last = input("Enter the last name: ")
        email_id=input("Enter the email id: ")
        try:
            sql_insert_query = f"INSERT INTO {table}(first_name,last_name,email) VALUES ({first},{last},{email_id})"
            my_cursor.execute(sql_insert_query)
            mydb.commit()
            print("Record inserted successfully")
    
        except mysql.connector.Error as error:
            print("Failed to update record to database: {}".format(error))
        finally:
            if (mydb.is_connected()):
                my_cursor.close()
                mydb.close()
                print("MySQL connection is closed")
        
        
    elif table_name == "papers":
        table = input("Enter the name of the table: ")
        title_report = input("Enter the title of the report: ")
        grade_report = input("Enter the grade of the report: ")
        studentid = input("Enter the student id: ")
        try:
            sql_insert_query = f"INSERT INTO {table}(title,grade,student_id) VALUES ({title_report},{grade_report},{studentid})"
            my_cursor.execute(sql_insert_query)
            mydb.commit()
            print("Record inserted successfully")
    
        except mysql.connector.Error as error:
            print("Failed to update record to database: {}".format(error))
        finally:
            if (mydb.is_connected()):
                my_cursor.close()
                mydb.close()
                print("MySQL connection is closed")
    else:
        print("Table not found")

def update_block():
    table_name = input("Enter the name of the table: ")
    column_update = input("Enter the column name where data has to be updated: ")
    name = input("Enter the new name : ")
    column_name = input("Enter the column where the operation is to be performed: ")
    
    column_value = input("Enter the row value: ")


    try:
        sql_update_query = f"""Update {table_name} set {column_update} = {name} where {column_name} = {column_value}"""
        my_cursor.execute(sql_update_query)
        mydb.commit()
        print("Record Updated successfully ")


    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if (mydb.is_connected()):
            my_cursor.close()
            mydb.close()
            print("MySQL connection is closed")

def delete_block():
    table_name = input("Enter the table name: ")
    column_name = input("Enter the column name: ")
    row_value = input("Enter the row value: ")
    try:
        
        sql_delete_query = f"""Delete from {table_name} where {column_name} = {row_value}"""
        my_cursor.execute(sql_delete_query,)
        mydb.commit()
        print("Record Deleted successfully ")

    except mysql.connector.Error as error:
        print("Failed to Delete record from table: {}".format(error))
    finally:
        if (mydb.is_connected()):
            my_cursor.close()
            mydb.close()
            print("MySQL connection is closed")
# insert_key()
# # delete_block()
# # update_block()