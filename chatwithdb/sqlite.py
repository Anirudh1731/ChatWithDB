import sqlite3

#Code to coonect sqlite
connection=sqlite3.connect('student.db')

#Create a cursor to insert record,create table
cursor=connection.cursor()


#create table

table_info='''
CREATE TABLE STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT)
'''

cursor.execute(table_info)

#Insert some more records
cursor.execute('''Insert Into STUDENT values('Anirudh','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Yashraj','Robotics','A',92)''')
cursor.execute('''Insert Into STUDENT values('Varun','Software Testing','B',93)''')
cursor.execute('''Insert Into STUDENT values('Puneet','AI','A',94)''')

#Display all records
print("The inserted records are")
data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

#Commit your changes in the database
connection.commit()
connection.close()
