import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendNotification():
    recepients_list = ""
    subject = 'Subject'
    message = "Message" 
    sendemail(recepients_list,subject,message)

def sendemail(to_addr_list, subject, message):
    username = ''
    password = ''   
    from_addr = ''    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    newmessage = '\r\n'.join([
              'To: %s' %recepient_list,
               'From: %s' % from_addr,
                'Subject: %s' %subject,
                '',
                message
                ])
    try:    
        server.sendmail(from_addr, to_addr_list,newmessage)
        print('notification sent')
    except:
        print ('error sending notification')
    server.quit()


sendNotification()