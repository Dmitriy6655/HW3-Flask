from flask import Flask
from hw_3.models import db, User
import click

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

# команда для создания БД

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("add-danil")
def add_user():
    user = User(username='danil',
                surname="finoskin",
                email='dan55@example.com',
                password="sds64d6sd6s5d")
    db.session.add(user)
    db.session.commit()
    print('Ivan add in DB!')

if __name__ == '__main__':
    app.run(debug=True)