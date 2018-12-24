import smtplib

#connect to smtp server
connection = smtplib.SMTP('smtp.gmail.com', 587)

#check connection to SMTP server
print(connection.ehlo())

#start TLS encryption
connection.starttls()

#pass credentials
connection.login('jane.doe@gmail.com', 'PASSWORD')

#send a email FROMM - TO - headers (subject then 2 line breaks to get to body) - body
connection.sendmail('jane.doe@gmail.com', 'john.doe@gmail.com', 'subject: Test\n\nThis should only go to outlook')

#close the connection
connection.quit()

