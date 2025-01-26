from flask import Flask, make_response, jsonify, request
from database import carros

# Abaixo vamos instanciar o Flask, ou seja, vamos criar uma variável que vai receber a nossa importaçao do Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# Isso serve para fazer com que o Flask nao mude a ordem das Keys, PARA ORDEM ALFABÉTICA!


# Mas para que o Flask saiba oque fazer com a funçao temos que usar um decorador, onde passamos a rota da API e o método
@app.route('/carros', methods=['GET'])
# Abaixo criei uma funçao que vai imprimir a lista de carros da nossa DataBase
def get_carros():
    return make_response(jsonify(
        message='Lista de Carros',
        data=carros))


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    carros.append(carro)
    return make_response(jsonify(
        message='Carro cadastrado com Sucesso',
        data=carro))

# Abaixo vamos startar a API, ou seja, deixar ela no ar
app.run()