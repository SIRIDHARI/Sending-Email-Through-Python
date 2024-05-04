import smtplib
import getpass
from email.mime.text import MIMEText

def send_email():
    sender_address='kk5306@srmist.edu.in'
    password=getpass.getpass()
    subject='Email Sending through Python'
    msg='''
     I am Siri Dhari
     and this is my project 
     *Email Sending through Python*
     Thank you
     '''
    #server initialisation
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    
    #login to SMTP server
    server.login(sender_address,password)
    
    #draft message
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=sender_address
    msg['To']='kk5306@srmist.edu.in'
    recipients='kk5306@srmist.edu.in'
    #send email
    server.sendmail(sender_address,recipients,msg.as_string())
    server.quit()
send_email()
