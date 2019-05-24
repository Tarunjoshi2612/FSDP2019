# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:51:10 2019

@author: Tarun Joshi
"""

# mysql

import mysql.connector
conn = mysql.connector.connect ( user='root', password='', host='localhost')
c = conn.cursor()
c.execute("CREATE DATABASE stu1;")
c.execute("USE stu1;")

c = conn.cursor()
c.execute ("""CREATE TABLE student(
          Student_Name TEXT, 
          Student_Age INTEGER,
          Student_Roll_no INTEGER, 
          Student_Branch TEXT
          )""")

c.execute("INSERT INTO student VALUES ('Tarun Joshi', 21, 1,'IT')")
c.execute("INSERT INTO student VALUES ('Yash Gupta',40,2,'IT')")
c.execute("INSERT INTO student VALUES ('Utkarsh Sharma', 21,3,'IT')")
c.execute("INSERT INTO student VALUES ('Prajjawal Kansal', 21,4,'IT')")
c.execute("INSERT INTO student VALUES ('Abhishek Garg', 21,5,'Cse')")

c.execute("SELECT * FROM student")
print ( c.fetchall() )