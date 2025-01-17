from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    numbers = list(range(1, 11))
    return render_template('index.html', numbers=numbers)

if __name__ == '__main__':
    app.run(port=5000)
