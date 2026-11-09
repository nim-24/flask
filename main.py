from flask import Flask
from flask import request
from markupsafe import escape
from flask import abort, redirect, url_for
from flask import render_template
from 

import database

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_post()
    else:
        return login_get()

def login_get():
    return render_template('login.html')

def login_post():
    class_name = request.form.get('class_name')
    places = request.form.get('places')
    db = insert_classes(class_name, places)
    db.select_all()
    error = "недостаточно данных"
    return render_template('login.html', class_name=class_name, places=places, error=error)

def search(a,b):
    return a==b

if __name__ == '__main__':
    db = Database('localhost', 'root', '<admin>', '<academy>')
    app.run(host='0.0.0.0', port=8080, debug=True)
