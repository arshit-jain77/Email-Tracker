from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client['talenq']

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_ID = 'tigersem4D@gmail.com'
PASSWORD = 'xxxxxxxxxxxx'
To_ = 'arshitjain6@gmail.com'
sub = 'mongo mail_15'
mssg = 'mongo mail body'

msg = MIMEMultipart('alternative')
msg['Subject'] = sub
msg['From'] = GMAIL_ID
msg['To'] = To_
import numpy
unique_code = str(numpy.random.randint(1000,1000000))

text = mssg
html = """
<html>
  <head></head>
  <body>
    <p>Happy 15</p>
    <img src = "https://32641f80d99a.ngrok.io/email-track?code=""" + unique_code+"""\" width='1' height='1'/>
  </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(part2)

mail_ = smtplib.SMTP('smtp.gmail.com', 587)
mail_.starttls()
mail_.login('tigersem4D@gmail.com', 'xxxxxxxx')
mail_.sendmail(GMAIL_ID, To_, msg.as_string())
mail_.quit()

mails = db.mails

mail = {
    'from_' : GMAIL_ID,
    'to_' : To_,
    'sub' : sub,
    'mssg' : mssg,
    'track_status' : 'no',
    'unique_code' : unique_code
}

mails.insert_one(mail)

print("Done")
