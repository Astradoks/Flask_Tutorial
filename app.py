from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/flask_tutorial'
app.secret_key = 'this_is_a_secret'
db = SQLAlchemy(app)

from controllers.datesController import *

if __name__ == '__main__':
    app.run(debug=True)