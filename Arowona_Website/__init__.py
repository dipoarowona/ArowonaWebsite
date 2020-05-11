# -*- coding: utf-8 -*-

from flask import Flask 
from flask_mail import Mail
from Arowona_Website.config import Config
#import config page later



app = Flask(__name__)
app.config["SECRET_KEY"] = Config.secret_key
app.config["MAIL_SERVER"] = Config.mail_sever
app.config["MAIL_PORT"] = Config.mail_port
app.config["MAIL_USE_TLS"] = Config.mail_use_tls
app.config["MAIL_USERNAME"] = Config.mail_username
app.config["MAIL_PASSWORD"] = Config.mail_password


mail = Mail(app)

from Arowona_Website import routes
