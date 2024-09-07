import smtplib
from email.mime.text import MIMEText

body = "This is a test email. How are you?"
msg = MIMEText(body)
msg['From'] = "lucia.ricciuti@gmail.com"
msg['To'] = "liukah@libero.it"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("lucia.ricciuti@gmail.com", "kospktyifojdihxq")
server.send_message(msg)

print("Email has been sent")

server.quit()