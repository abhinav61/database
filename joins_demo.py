import mysql.connector
import time


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

def select_s():

    name = input("Enter the name of the table: ")
    my_cursor.execute(f"SELECT * FROM {name}")

    myresult = my_cursor.fetchall()

    for x in myresult:
        print(x)

def join_script(): #join operation on two tables

    column_1 = input("Enter the first column: ")
    column_2 = input("Enter the second column: ")
    table_name = input("Enter the table name: ") 
    join_name = input("Enter the Join name: ")
    table_name_2 = input("Enter the second table name: ")
    First_Foriegn_key = input("Enter the first foriegn key: ")
    second_Foriegn_key = input("Enter the second foriegn key: ")

    sql = f"SELECT {column_1}, {column_2} from {table_name} {join_name} {table_name_2} ON {First_Foriegn_key} = {second_Foriegn_key};"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    mydb.commit()
    for x in result:
        print(x)

def join_operation(): #join operations on two tables using clauses

    column_1 = input("Enter the first column: ")
    column_2 = input("Enter the second column: ")
    column_3 = input("Enter the third column: ")
    table_name = input("Enter the table name: ") 
    join_name = input("Enter the Join name: ")
    table_name_2 = input("Enter the second table name: ")
    First_Foriegn_key = input("Enter the first foriegn key: ")
    second_Foriegn_key = input("Enter the second foriegn key: ")
    clause_1 = input("Enter the first clause: ")
    clause_column = input("Enter the clause column: ")
    clause_2 = input("Enter the second clause: ")
    clause_name = input("Enter the clause column: ") 
    
    sql = f"SELECT {column_1}, {column_2}, {column_3} from {table_name} {join_name} {table_name_2} ON {First_Foriegn_key} = {second_Foriegn_key} {clause_1} {clause_column} {clause_2} {clause_name};"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    mydb.commit()
    for x in result:
        print(x)

def join_operations():  #join operations on three tables using clauses

    column_1 = input("Enter the first column: ")
    column_2 = input("Enter the second column: ")
    column_3 = input("Enter the third column: ")
    table_name = input("Enter the table name: ") 
    join_name = input("Enter the Join name: ")
    table_name_2 = input("Enter the second table name: ")
    First_Foriegn_key = input("Enter the first foriegn key: ")
    second_Foriegn_key = input("Enter the second foriegn key: ")
    join_name_1 =  input("Enter the join name: ")
    table_name_3 = input("Enter the third table: ")
    First_Foriegn_keys = input("Enter the first foriegn key: ")
    second_Foriegn_keys = input("Enter the second foriegn key: ")
    clause_1 = input("Enter the first clause: ")
    clause_column = input("Enter the clause column: ")
    clause_2 = input("Enter the second clause: ")
    clause_name = input("Enter the clause column: ") 
    
    sql = f"SELECT {column_1}, {column_2}, {column_3} from {table_name} {join_name} {table_name_2} ON {First_Foriegn_key} = {second_Foriegn_key} {join_name_1} {table_name_3} ON {First_Foriegn_keys} = {second_Foriegn_keys} {clause_1} {clause_column} {clause_2} {clause_name};"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    mydb.commit()
    for x in result:
        print(x)

t0 = time.time()
# select_s()
# join_script()
# join_operation()
# join_operations()

t1 = time.time()

total_n = t1-t0
print(total_n)