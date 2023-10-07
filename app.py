from pprint import pprint

from flask import Flask, request

app = Flask(__name__)

# a definição do método post faz com que essa rota não responda mais com get, ou seja,
# tentar acessá-la no navegador irá resultar em 405 - método não permitido

@app.route('/cadastro', methods=['post'])
def cadastro():
    # objeto request é criado pelo flask e contém todos os dados da requisição recebida pelo servidor
    pprint(vars(request))
    # request.form é um dicionário com os valores que foram enviados pelo formulário
    pprint(request.form)
    return 'ok', 200


if __name__ == '__main__':
    app.run(debug=True)
