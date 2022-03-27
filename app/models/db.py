from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, unique=True, nullable=False)
    endereco = db.Column(db.String, nullable=False)
    data_nascimento = db.Column(db.DateTime, nullable=False)
    login = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)


    def __init__(self, nome, cpf, endereco, data_nascimento, login, senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.login = login
        self.senha = senha

    def __repr__(self):
        return '<User %r>' % self.nome