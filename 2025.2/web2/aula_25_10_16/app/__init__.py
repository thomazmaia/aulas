from flask import Flask

app = Flask(__name__)

# Importação de Controllers depois da criação do app
from app.controllers import homepage