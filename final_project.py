import getpass
import smtplib
<<<<<<< HEAD:final_project.py
import os
=======
>>>>>>> refs/remotes/origin/main:Final-Project/final_project.py
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

f = open("receiver_list.txt", "a")

f.write("m.rizqy@sci.ui.ac.id""\n")
f.write("muhammadrizqy.septyandy@gmail.com""\n")

email_receiver = open("receiver_list.txt").read().splitlines()
email_sender = input('Masukkan Alamat Email Anda: ')
password = getpass.getpass()

f.close()

# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = email_sender
  
# storing the receivers email address  
msg['To'] = ", ".join(email_receiver)
  
# storing the subject  
msg['Subject'] = "Basic Python Final Project"
  
# string to store the body of the mail 
body = """\
    Hi....,
    
    This is an automatic message from Basic Python Final Project
    For more information, please visit to:
    https://github.com/septyandy08

    Thanks Before

    Muhammad Rizqy Septytandy
    Department of Geosciences
    Universitas Indonesia"""
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent  
with open('G:\\Desktop\welcome.txt', 'rb') as txt:
    txt_1 = MIMEBase("application", "octet-stream")
    txt_1.set_payload(txt.read())
    encoders.encode_base64(txt_1)
    txt_1.add_header('Content-Disposition', 'attachment', filename= "welcome.txt")
    msg.attach(txt_1)

with open('G:\\Desktop\Pyroclastic_Flow_St._Helens.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename="Pyroclastic_Flow_St._Helens.jpg")
    msg.attach(img)

with open('G:\\Desktop\Absensi.pdf', 'rb') as attachment:
    pdf = MIMEBase("application", "octet-stream")
    pdf.set_payload(attachment.read())
    encoders.encode_base64(pdf)
    pdf.add_header('Content-Disposition', 'attachment', filename= "Absensi.pdf")
    msg.attach(pdf)

# creates SMTP session 
new_txt = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
new_txt.starttls() 
  
# Authentication 
new_txt.login(email_sender, password) 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
new_txt.sendmail(email_sender, email_receiver, text) 
  
# terminating the session 
new_txt.quit()
<<<<<<< HEAD:final_project.py


file_path = "receiver_list.txt"

if os.path.exists(file_path):
    os.remove("receiver_list.txt")
    print("file " + file_path + " deleted")
else:
    print("file not exist")
=======
>>>>>>> refs/remotes/origin/main:Final-Project/final_project.py
