"""
This script can be used to see if any open ports are returning any HTTP data
Put your list of ports into "ports.txt" 
Run the .py and enter the IP
It will output:

"yourIP:port-on-line-1" 
"yourIP:port-on-line-2"
etc

Open CMD and paste the contents of "output.txt" into the CMD window
It will open each link in a new tab in your default web browser
"""

import subprocess

p = open("ports.txt", "r")
o = open("output.txt", "w")

ip = raw_input("Enter the IP: ")

for line in p.readlines():
    o.write("start " + "http://" + ip + ":" + (line) +
            "start " + "https://" + ip + ":" + (line))

p.close()
o.close()

subprocess.call(["Notepad.exe", "output.txt"])
