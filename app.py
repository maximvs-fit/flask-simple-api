from pprint import pprint

from flask import Flask, request, redirect

app = Flask(__name__)

# a definição do método post faz com que essa rota não responda mais com get, ou seja,
# tentar acessá-la no navegador irá resultar em 405 - método não permitido

@app.route('/cadastro', methods=['post'])
def cadastro():
    # objeto request é criado pelo flask e contém todos os dados da requisição recebida pelo servidor
    pprint(vars(request))
    # request.form é um dicionário com os valores que foram enviados pelo formulário
    pprint(request.form)

    # retorna um redirecionamento para a página inicial do form
    response = redirect('http://localhost:5500/sucesso.html')
    return response


@app.route('/teste/<nome>', methods=['post'])
def teste_2(nome):
    print(nome, type(nome))
    # pprint(vars(request))
    return {'msg': 'ok texto'}, 200

@app.route('/teste/<int:id>', methods=['post'])
def teste(id):
    print(id, type(id))
    # pprint(vars(request))
    return {'msg': 'ok numero'}, 200



if __name__ == '__main__':
    app.run(debug=True)
