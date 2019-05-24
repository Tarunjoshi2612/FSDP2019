# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:26:08 2019

@author: Tarun Joshi
"""

# sqlite

import sqlite3

conn = sqlite3.connect ( 'stu.db' )

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