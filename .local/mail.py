import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders


SENDER = "duys@pioneerrd.com"
PASSWORD = "Dawie2018"

SIGNATURE = \
        """

Duan Uys, MSc
R&D Engineer
210-400-6139
        """

if __name__ == "__main__":
    message = MIMEMultipart()
    message['From'] = SENDER
    
    to_address = input("Receiver Address: ")
    to_address = ",".join([x.strip() for x in to_address.split(",")])

    message['To'] = to_address 

    message['Subject'] = input("Subject: ")

    message.attach(MIMEText(input("Body:\n") + SIGNATURE, 'plain'))
    
    attachment = input("Do you have anything to attach?: ")

    if attachment.lower()[0] == 'y':
        attachment_name = input("Attachment Name: ")

        attach_file=MIMEApplication(open(attachment_name, "rb").read())
        attach_file.add_header('Content-Disposition', 'attachment', filename=attachment_name)
        message.attach(attach_file)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(SENDER, PASSWORD)
    text = message.as_string()

    print("Sending email...", end='')
    session.sendmail(SENDER, to_address, text)
    session.close()
    print("Success")
    

