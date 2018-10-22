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
