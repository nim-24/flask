from flask import Flask, request, abort, redirect, url_for, render_template #pip install flask
from markupsafe import escape
from database import Database

app = Flask(__name__) #все принадлежит фласку

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login_btn = request.form['login']
        if login_btn == 1:
            return login_get()
        register_btn = request.form['register']
        if register_btn == 2:
            return register_get()
    return render_template('index.html')

def register():
    if request.method == 'POST':
        return register_post()
    else:
        return render_template('register.html')

def register_post():
    reg_email = request.form['reg_email']
    reg_password = request.form['reg_pass']

def register_get():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST']) #маркер для кнопки на роутер
def login():
    if request.method == 'POST':
        return login_post()
    else:
        return login_get()

def login_get():
    return render_template('login.html')

def login_post():
    class_name = request.form.get['class_name']
    places = request.form.get['places']
    db = insert_classes(class_name, places)
    db.select_all()
    error = "недостаточно данных"
    return render_template('login.html', class_name=class_name, places=places, error=error)

def search(a,b):
    return a==b

if __name__ == '__main__':
    db = Database('localhost', 'root', 'admin', 'academy')
    app.run(host='0.0.0.0', port=8080, debug=True)
