from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)
...




@app.route('/')
def index():
    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True)