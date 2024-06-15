import sqlite3
import sys
from os.path import exists

if exists("cs_course_scheduling.sqlite"):
    conn = sqlite3.connect('cs_course_scheduling.sqlite')
    #cursor = conn.execute("SELECT first_name, last_name, academic_year FROM students")
    #cursor = conn.execute("SELECT first_name, last_name, academic_year FROM students ORDER BY last_name ASC")
    cursor = conn.execute("SELECT first_name, last_name, academic_year FROM students WHERE academic_year = "+sys.argv[1])
    print("<!DOCTYPE html>")
    print("<html>")
    print("<body>")
    print("<table border = '1'>")
    print("<tr>")
    print("<th>First Name</th>")
    print("<th>Last Name</th>")
    print("<th>Year</th>")
    print("</tr>")
    for row in cursor:
        print("<tr>")
        print("<td>",row[0],"</td>")
        print("<td>",row[1],"</td>")
        print("<td>",row[2],"</td>")
        #print ("First Name = ", row[0])
        #print ("Last Name = ", row[1])
        #print ("Academic Year = ", row[2])
        print("</tr>")
        #print ("----------------------------------------")

    print("</body>")
    print("</html>")
    conn.close()
    #print("Database was accessed and closed")

else:
    print('Database file cs_course_scheduling.sqlite not found in current working directory.')
