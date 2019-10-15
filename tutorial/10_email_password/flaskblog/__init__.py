import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '347a46e3df6aca9b2cda78f4b5fd556add82d01494c35ef307491ba98ae143d2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# I can get the gmail solution to work using app passwords
# https://stackoverflow.com/questions/37058567/configure-flask-mail-to-use-gmail
# https://security.google.com/settings/security/apppasswords
# office365 may need additional steps
app.config['MAIL_USERNAME'] = os.environ.get('USER_NAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)

from flaskblog import routes
