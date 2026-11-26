from flask import Flask, request, render_template, session
from databases import Database

app = Flask(__name__)
app.secret_key = "change-me-to-a-random-secret"

numbers = [number for number in range(20) if number % 2 == 0]

products = {"хлеб": 50, "молоко": 90, "яблоки": 120}
products["молоко"] = 95

tags = set(["python", "flask", "python", "данные", "flask"])

point = (10, 20)

squares_loop = []
for number in range(1, 6):
    squares_loop.append(number ** 2)
squares_comprehension = [number ** 2 for number in range(1, 6)]


def print_examples():
    print("1. Чётные числа:", numbers)
    print("2. Товары и цены:")
    for product, price in products.items():
        print(f"   {product}: {price} руб.")
    print("3. Множество без повторов:", tags)
    print("   'python' есть в множестве:", "python" in tags)
    print("4. Координаты:", point)
    try:
        point[0] = 99
    except TypeError as error:
        print("   Кортеж неизменяем:", error)
    print("5. Квадраты (цикл):", squares_loop)
    print("   Квадраты (comprehension):", squares_comprehension)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    login_name = request.form.get('log_name', '').strip()
    login_password = request.form.get('log_pass', '')
    if db.select_users(login_name, login_password) is not None:
        return "Ура, вы вошли"
    return render_template('login.html', error='Неверный пароль или логин')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    email = request.form.get('reg_email', '').strip()
    password = request.form.get('reg_pass', '')
    if not email or not password:
        return render_template('register.html', error='Заполните почту и пароль.')
    try:
        db.create_user(email, password)
    except Exception:
        return render_template(
            'register.html',
            error='Не удалось зарегистрироваться. Возможно, эта почта уже занята.'
        )
    session['user_email'] = email
    return render_template('profile.html', email=email)


if __name__ == '__main__':
    print_examples()
    db = Database('localhost', 'root', 'root', 'academy')
    app.run(host='0.0.0.0', port=15000, debug=True)
