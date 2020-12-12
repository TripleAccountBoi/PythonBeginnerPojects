import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# following tutorial

# Setting up email variables
port = 465
email_sender = "my@email.com"
email_receiver = "your@email.com"
password = input("Type your password: ")
subject = "An email with an attachment sent through Python"
body = "This is an email with an attachment sent through Python"

# Setting up a mime object that sends multiple types of data

message = MIMEMultipart()
message["Subject"] = subject
message["From"] = email_sender
message["To"] = email_receiver
message["Bcc"] = email_receiver


# Attaching the plain text
message.attach(MIMEText(body, 'plain'))

# Path to the document to be attached
filename = 'yourdocument.extension'

# Open document as binary for reading

with open(filename, 'rb') as attachment:
    # Assigning a MIMEBase object that accepts applications to part
    part = MIMEBase("application", "octet-stream")
    # Transferring the content of the document to part
    part.set_payload(attachment.read())

# Encoding as base64 so it can be read by the email provider - I think
encoders.encode_base64(part)

# No idea honestly
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Attaching the attachment to the email
message.attach(part)
text = message.as_string()


# log into gmail and send mail
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(email_sender, password)
    server.sendmail(email_sender, email_receiver, text)
