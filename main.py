from flask import Flask

# Abaixo vamos instanciar o Flask, ou seja, vamos criar uma variável que vai receber a nossa importaçao do Flask

app = Flask(__name__)

# Abaixo vamos startar a API, ou seja, deixar ela no ar

app.run()