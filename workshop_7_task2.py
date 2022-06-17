#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:18:37 2020
@author: WillCrane
"""
# Task 2, Week 7
import sqlite3
# Checks for the Database in the Directory
connection = sqlite3.connect("hotel.db")
cursor = connection.cursor()

## - List full details of all hotels in Brisbane. - ##
# Checks all the Hotels Located in Brisbane
sql_command_question1 = """
SELECT *
FROM Hotel
WHERE city = "Brisbane"
"""
# Searches the database using sql_command_question1
cursor.execute(sql_command_question1)
# Prints Brisbane Hotels:
print("Brisbane Hotels: ")
# Stores Information Retrieved from sql_comman_question1
result1 = cursor.fetchall()
# Prints all the Brisbane Hotels
for r1 in result1:
    print(r1)
    
## - List the names and addresses of all guests in ascending order of guest names. - ##    
# Checks all the Guest Details Located in the Database
sql_command_question2 = """
SELECT guestName, guestAddress
FROM Guest
ORDER BY guestName ASC
"""
# Searches the database using sql_command_question2
cursor.execute(sql_command_question2)
# Prints Guests:
print("Guests:")
# Stores Information Retrieved from sql_comman_question2
result2 = cursor.fetchall()
# Prints all data found in the result2 variable 
for r2 in result2:
    print(r2)
    
## - List the price and type of all rooms at the Grosvenor Hotel - ##
# Checks all the Grosvenor Hotel Room Details
sql_command_question3 = """
SELECT r.roomtype, r.price
FROM Room r, Hotel h
WHERE h.hotelName = "Grosvenor Hotel" 
AND r.hotelNo = h.hotelNo
"""
# Searches the database using sql_command_question3
cursor.execute(sql_command_question3)
# Prints Hotel Details
print("Hotel Details:")
# Stores Information Retrieved from sql_comman_question3
result3 = cursor.fetchall()
# Prints all data found in the result3 variable 
for r3 in result3:
    print(r3)
    
    