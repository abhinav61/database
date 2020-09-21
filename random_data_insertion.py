import os
import mysql.connector
import time
import random


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
def project1():
    name = ['r1','r2','r3','r4','r5']
    employee = ['John','Harry','Max','Dan']
    associatedgroups = ['Testing','Designing','Developer']
    State = ['Added','Updated','Deleted']
    sql_statement = "INSERT INTO ProjectRevision(project_id,prj_rev_name,created_by,associated_groups,state) VALUES (%s,%s,%s,%s,%s)"
    for i in range(50000):
        v1 = random.randint(1000,9999)
        v2 = random.choice(name)
        v3 = random.choice(employee)
        v4 = random.choice(associatedgroups)
        v5 = random.choice(State)

        my_cursor.execute(sql_statement, (v1, v2,v3, v4, v5))
    mydb.commit()

def project2():
    my_cursor.execute("CREATE TABLE IF NOT EXISTS block(block_id INT AUTO_INCREMENT PRIMARY KEY, prj_rev_id INT, block_name VARCHAR(50), dft_engineer VARCHAR(20), test_engineer VARCHAR(20), design_engineer VARCHAR(20), created_date TIMESTAMP DEFAULT NOW(), created_by VARCHAR(20), associated_groups VARCHAR(200), state VARCHAR(200))")
    blockname = ['ATPG','VLSI','ATG']
    dftengineer = ['Sam','Samuel','Sammy']
    testengineer = ['Rahul','Varun','Vipin']
    designengineer = ['John','Harry','Max','Dan']
    createdby = ['A','B','C']
    associatedgroups = ['Testing','Designing','Developer']
    State = ['Added','Updated','Deleted']
    sql_statement = "INSERT INTO block(prj_rev_id,block_name,dft_engineer,test_engineer,design_engineer,created_by,associated_groups,state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    for i in range(100000):
        v1 = random.randint(1000,9999)
        v2 = random.choice(blockname)
        v3 = random.choice(dftengineer)
        v4 = random.choice(testengineer)
        v5 = random.choice(designengineer)
        v6 = random.choice(createdby)
        v7 = random.choice(associatedgroups)
        v8 = random.choice(State)
        my_cursor.execute(sql_statement, (v1, v2,v3, v4, v5,v6,v7,v8))
    mydb.commit()

t0 = time.time()
# project1()
project2()
t1 = time.time()

total_n = t1-t0
print(total_n)