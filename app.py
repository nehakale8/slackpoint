from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:vansh@localhost/slackpoint"
db = SQLAlchemy(app)


@app.route('/')
def basic():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug = True)
