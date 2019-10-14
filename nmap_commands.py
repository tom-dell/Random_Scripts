"""
This is a simple script I wrote to help gather information when doing simple vulnerability scans.


This will generate a few commands that you can paste directly into nmap, it will output the command you choose during selection, it will also use the IP in the naming of the text file, as well as place it in your user drive.

###############Instructions###############

1. enter the ip address of the host, it will use this IP in the naming of the text files
2. type a name in
3. choose which nmap command you want
4. type username, or choose from list
5. press enter
6. notepad will open with the command ready to paste into nmap


#########################################################################################
                            SSL output                                                  #
                                                                                        #
Where test-user-name is the name entered, and 10.10.10.10 is the IP entered             #
                                                                                        #
                                                                                        #
nmap -oN c:\users\test-user-name\10.10.10.10-ssl.txt --script ssl* 10.10.10.10          #
                                                                                        #
#########################################################################################


############################################################################################
                            SSh output                                                     #
                                                                                           #
Where test-user-name is the name entered, and 10.10.10.10 is the IP entered                #
                                                                                           #
                                                                                           #
nmap -oN c:\users\test-user-name\10.10.10.10-ssh.txt --script ssh2-enum-algos 10.10.10.10  #
                                                                                           #
############################################################################################
"""


import os
o = open("output.txt", "w")

print("This script generates a NMap command, that you paste into a NMap console, which when ran will start a extensive scan against the IP entered, and then save the scan results to your home directory (if the username you is your username on the PC)")
print("view the read-me for more information")

# ask for the IP, and then asks if the user wants to enter name, or choose
ip = input("Enter the IP: ")
command = input("Press 1 for SSL checks, press 2 for SSH checks: ")

# generate SSL command string
if command == "1":
    name = input("Enter your username on this host: ")
    o.write("nmap -oN c:\\users\\" + name + "\\" +
            ip + "-ssl.txt" + " --script ssl* " + ip)


# generate SSH command string
if command == "2":
    name = input("Enter your username on this host: ")
    o.write("nmap -oN c:\\users\\" + name + "\\" + ip +
            "-ssh.txt" + " --script ssh2-enum-algos " + ip)


# close output.txt, open notepad and output.txt
o.close()
osCommandString = "notepad.exe output.txt"
os.system(osCommandString)
