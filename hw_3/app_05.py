from flask import Flask, render_template, request, redirect, url_for
from hw_3.forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect
from hw_3.models import db, User
from hashlib import sha256

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abe82aafb8a4dd91b6d2e0565ad6d639a0aaae71b06922407d6c25b621abb67d'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

"""
Секретный ключ
Небольшое отступление. Чтобы не получать ошибки вида при работе с сессией
RuntimeError: The session is unavailable because no secret key
was set. Set the secret_key on the application to something
unique and secret.
необходимо добавить в Flask приложение секретный ключ.
Простейший способ генерации такого ключа, выполнить следующие пару строк
кода
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hello!'



@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        user = User(username=form.username.data,
                    surname=form.surname.data,
                    email=form.email.data,
                    password = sha256(form.password.data.encode(encoding="utf-8")).hexdigest())
        db.create_all()
        db.session.add(user)
        db.session.commit()
        pass
        # return redirect(url_for('register'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
