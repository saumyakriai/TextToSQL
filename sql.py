import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")

#create a cursor object to insert,record,create table,retrieve
cursor = connection.cursor()

#create a table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25),
MARKS INT); """

cursor.execute(table_info)

#insert records
cursor.execute("insert into STUDENT values('Saumya','Bussiness Analytics','A',77)")
cursor.execute("insert into STUDENT values('Monica','Information System','C',97)")
cursor.execute("insert into STUDENT values('Shikha','CSE ','A',79)")
cursor.execute("insert into STUDENT values('Vani','Bussiness Analytics','B',81)")
cursor.execute("insert into STUDENT values('Suman','MIS','A',55)")

#display all records
print("Inserted records are")

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)


#close the connection
connection.commit()
connection.close()
