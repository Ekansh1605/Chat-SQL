import sqlite3

## connect to sqllite
connection=sqlite3.connect("student1.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Ekansh','Data Science','B',96)''')
cursor.execute('''Insert Into STUDENT values('Sarthak','Data Science','A',100)''')
cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Jonas','DEVOPS','A',35)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()