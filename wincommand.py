""" 
This is a simple script I wrote to help gather information when doing simple vulnerability scans.


This will generate a few commands that you can paste directly into windows to create text files with relevant information about the host, aswell as open the user/groups page in computer management and open your user drive on the host (where the text files are saved)

###############Instructions###############

1. enter the ip address of the host, it will use this IP in the naming of the text files
2. follow the name prompts, this way it'll open the correct location of where the text files get saved, at the end
3. press enter
4. output.txt will open the commands
5. paste those commands into windows CMD
6. press enter


#########################################################################################################################
                                                                                                                        #
                                                   OUTPUT                                                               #
                       Where 10.10.10.10 is the IP and tom is the username entered                                      #
                                                                                                                        #
                                                                                                                        #
net accounts > 10.10.10.10accounts.txt  -----will create a text file in your user drive showing the password policy     #
netstat -a > 10.10.10.10ports.txt -----------will create a text file in your user drive showing the ports               #
C:\Windows\System32\lusrmgr.msc -------------opens the users/group page in computer management                          #
explorer c:\users\tom -----------------------open the path where the text files are saved                               #
                                                                                                                        #
######################################################################################################################### 
"""


import os
o = open("output.txt", "w")

# ask for the IP, and then asks if the user wants to enter name, or choose
ip = input("enter the IP: ")
name = input("Press 1 to enter a name, press 2 to skip (this will not add the command to open the location of the text files). ")

# user will enter their own name, will write commands using entered name
if name == "1":
    name1 = input("enter your username on this host: ")
    o.write("net accounts > " + ip + "accounts.txt" + "\n" + "netstat -a > " + ip + "ports.txt" +
            "\n" + "C:\Windows\System32\lusrmgr.msc" + "\n" + r"explorer c:\users\\" + name1 + "\n")

if name == "2":
    o.write("net accounts > " + ip + "accounts.txt" + "\n" + "netstat -a > " +
            ip + "ports.txt" + "\n" + "C:\Windows\System32\lusrmgr.msc")

# close output.txt, open notepad and output.txt
o.close()
osCommandString = "notepad.exe output.txt"
os.system(osCommandString)
