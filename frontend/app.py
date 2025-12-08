from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/products')
def products_page():
    return render_template('products.html')

@app.route('/payment')
def payment_page():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
