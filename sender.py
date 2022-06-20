import pandas as pd
import smtplib

SenderEmail = input("Enter your email: ")
password = input("Enter your one time password: ")
file = input('Enter the File Name: ')

e = pd.read_excel(file)
emails = e['emails'].values
names = e['names'].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderEmail, password)

for email,name in zip(emails,names):
    subject = "Looking for a graphic designer"
    msg = f'''Hi {name.split(" ")[0]}, 
    Type Email Here'''

    body = "Subject: {}\n\n{}".format(subject,msg)
    server.sendmail(SenderEmail, email, body)
    print("done")
server.quit()
