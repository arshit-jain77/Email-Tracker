import smtplib
import pytracking
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "tigersem4D@gmail.com"
toaddr = "arshitjain6@gmail.com"
msg = MIMEMultipart()


msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "grande"
body = "bla bla bla"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('tigersem4D@gmail.com','xxxxxx')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

print('DONE')

# Pytracking
open_tracking_url = pytracking.get_open_tracking_url(
    {"customer_id": 1}, base_open_tracking_url="https://trackingdomain.com/path/",
    webhook_url="http://requestb.in/123", include_webhook_url=True)

print("open_tracking_url : ",open_tracking_url)

tracking_result = pytracking.get_open_tracking_result(open_tracking_url, base_open_tracking_url="https://trackingdomain.com/path/")
print("tracking_result : ",tracking_result)

from pytracking.webhook import send_webhook
send_webhook(tracking_result)


