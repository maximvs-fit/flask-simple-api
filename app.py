from flask import Flask

app = Flask(__name__)


@app.route('/cadastro')
def cadastro():
    return 'ok', 200


if __name__ == '__main__':
    app.run(debug=True)
