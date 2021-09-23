from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = '0c66fa3f6ef1ce2cce53c113e7686f92' #siski
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'newsportal_db'

mysql = MySQL()
mysql.init_app(app)