from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = "cd36a5df21f4d877d41f075a8dac7067"
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///site.db"


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "ojim07@gmail.com"
app.config['MAIL_PASSWORD'] = 'xhblwioqzppdyxrj'
mail = Mail(app)



bc = Bcrypt(app)
db = SQLAlchemy(app)
lm = LoginManager(app)
lm.login_view = "login"
lm.login_message_category ="info"

from App import routes