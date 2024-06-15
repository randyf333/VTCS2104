"""
@date: 
@author:
@PID: 
@assignment: W9 CW Reading data off html
"""

import re
# use regex to parse the html string and extract the target data
in_filename = 'student_list.html'
out_filename = 'student_list.txt'
# defines the name of the file that you're going to read and write into

content = open(in_filename,"r")
output = open(out_filename,"a")
# content and output are file stream object, you could use 'r'(read), 'w'(write) or 'a'(append)
 
str = content.read()
# read() method will turn a file stream into a regular string
pattern = r'<td>(\w*)<\/td>\s*<td>(\w*)<\/td>\s*<td>(\d)'
matches = re.findall(pattern,str)#returns list of tuples
matches.sort(key=lambda a: a[2])
for i in range(len(matches)):
    str = matches[i][1] + ", " + matches[i][0] + " " + matches[i][2]
    x = str.rjust(35)
    output.write(x + "\n")
# use matches = re.findall(pattern,str), you need to figure out what pattern to use
# pattern = r'<td>(\w*)<\/td>\s*<td>(\w*)<\/td>\s*<td>(\d)'
# once you get a match, you access different components from the match object using indices.
# use output.write() to write content to the output 
# for output formatting, you can try rjust()

output.close()
content.close()
#close the stream