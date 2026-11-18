from flask import Flask, request, abort, redirect, url_for, render_template #pip install flask
from markupsafe import escape
from databases import Database

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login_btn = request.form['login']
        if login_btn == "1":
            return login_get()
        register_btn = request.form['register']
        if register_btn == "2":
            return register_get()
    return render_template('index.html')

def register_get():
    return render_template('register.html')

def login_get():
    return render_template('login.html')
    

@app.route('/login', methods=['GET', 'POST']) #маркер для кнопки на роут
def login():
    if request.method == 'POST':
        return login_post()
    else:
        return login_get()

def login_post():
    user_login = request.form.get('log_name')
    user_password = request.form.get('log_pass')
    select = db.select_users(user_login, user_password)
    # valid_password = select['password']
    error = "неверные данные или пароль"
    message = "добро пожаловать"
    if select :
        return message
    else:
        return error


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return register_post()
    else:
        return register_get()

def register_post():
    reg_email = request.form.get('reg_email', '').strip()
    reg_password = request.form.get('reg_pass')

    # Не отправляем отсутствующие поля в MySQL: email в users имеет NOT NULL.
    if not reg_email or not reg_password:
        return render_template(
            'register.html',
            error='Почта или пароль не пришли из формы. Проверь name="reg_email" и name="reg_pass".'
        )

    user = db.get_user_by_email(reg_email)

    if user:
        return render_template(
            'register.html',
            error='Пользователь с такой почтой уже зарегистрирован'
        )

    db.insert_users(reg_email, reg_password)
    return render_template('profile.html')


if __name__ == '__main__':
    db = Database('localhost', 'root', 'root', 'academy')
    app.run(host='0.0.0.0', port=15000, debug=True)
