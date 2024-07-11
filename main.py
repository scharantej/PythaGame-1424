
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form.get('a'))
    b = float(request.form.get('b'))
    c = (a ** 2 + b ** 2) ** 0.5
    return render_template('result.html', a=a, b=b, c=c)

if __name__ == '__main__':
    app.run(debug=True)
