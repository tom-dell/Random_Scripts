"""
This script will convert a list of

1
2
3

to 1, 2, 3


Instructions

paste your list into input.txt
save input.txt
run listtoline.py
output.txt will open
replace the last "," with a "."
"""


import os

i = open("input.txt", "r")
o = open("output.txt", "w")


for line in i.readlines():
    o.write (line.replace("\n", ", "))

i.close()
o.close()


#open notepad output.txt
osCommandString = "notepad.exe output.txt"
os.system(osCommandString)
