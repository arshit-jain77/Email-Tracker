import pymysql
import smtplib
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, send_from_directory
import base64
from werkzeug import secure_filename, SharedDataMiddleware
import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

UPLOADER_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

def get_as_base64(url):
    return base64.b64encode(request.get(url).content)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/talenq'
db = SQLAlchemy(app)

class mail(db.Model):
    From_ = db.Column(db.String(25), primary_key=True)
    To_ = db.Column(db.String(25), nullable=False)
    sub = db.Column(db.String(100), nullable=False)
    mssg = db.Column(db.String(500), nullable=False)
    email_track_code = db.Column(db.String(500), nullable=False)

GMAIL_ID = 'tigersem4D@gmail.com'
PASSWORD = 'tiger@4D'

# Before running the program turn on less secure apps for tiger account

@app.route("/")
def talenq_html():
    return render_template('talenq_mail.html')

@app.route("/mainpage_signin.html", methods=['GET', 'POST'])
def mainpage_signin():

    if request.method == 'POST':

        GMAIL_ID = request.form.get('from')
        To_ = request.form.get('to')
        sub = request.form.get('sub')
        mssg = request.form.get('mssg')

        # track_code = np.random.randint(10000,1000000)
        track_code = str(123456)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = sub
        msg['From'] = GMAIL_ID
        msg['To'] = To_

        text = mssg
        html = """\
        <html>
          <head></head>
          <body>
            <p>Happy 15</p>
            <img src = "https://809e0d020e93.ngrok.io/email-track-arshit/email_track.php?code=123456" width='1' height='1'/>
          </body>
        </html>
        """

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)

        mail_ = smtplib.SMTP('smtp.gmail.com', 587)
        mail_.starttls()
        mail_.login('tigersem4D@gmail.com', 'tiger@4D')
        mail_.sendmail(GMAIL_ID, To_, msg.as_string())
        mail_.quit()

        entry = mail(From_=GMAIL_ID, To_=To_, sub=sub, mssg=mssg, email_track_code=track_code)
        db.session.add(entry)
        db.session.commit()

    return render_template('mainpage_signin.html')

if __name__ == '__main__':
    app.debug = False
    app.run()