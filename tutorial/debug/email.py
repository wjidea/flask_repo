from flask import Flask
from flask_mail import Mail, Message
import os
# instantiate flask app
app = Flask(__name__)

# set configuration and instantiate mail
mail_settings = {
    "MAIL_SERVER": 'smtp.office365.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'wjavac@hotmail.com',
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}
app.config.update(mail_settings)
mail = Mail(app)

# create message
msg = Message(subject='test',
              sender='wjavac@hotmail.com',
              recipients='wjidea@gmail.com',
              body='Hello World')

# change message ID
# msg.msgId = msg.msgId.split('@')[0] + '@short_string'  # for instance your domain name

# send email
mail.send(msg)