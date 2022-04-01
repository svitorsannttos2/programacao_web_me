from flask import Flask, Response, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/web_flask'
db = SQLAlchemy(app)
app.secret_key = 'web'


# Tabelas do banco de dados


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(11), unique=True)
    data_nascimento = db.Column(db.DateTime)
    endereco = db.Column(db.String(100))
    login = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, nome, cpf, data_nascimento, endereco, login, senha):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.login = login
        self.senha = senha


class Motorista(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(11), unique=True)
    data_nascimento = db.Column(db.DateTime)
    endereco = db.Column(db.String(100))

    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Passageiro(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(11), unique=True)
    data_nascimento = db.Column(db.DateTime)
    endereco = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    uf = db.Column(db.String(10))

    def __init__(self, nome, cpf, data_nascimento, endereco, cidade, uf):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf


class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(11), unique=True)
    tipo = db.Column(db.String(50))
    placa = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    capacidade = db.Column(db.Integer)

    def __init__(self, nome, cpf, tipo, placa, marca, modelo, ano, capacidade):
        self.nome = nome
        self.cpf = cpf
        self.tipo = tipo
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.capacidade = capacidade


class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    cpf = db.Column(db.String(11), unique=True)
    placa = db.Column(db.String(50))
    data_nascimento = db.Column(db.DateTime)
    km = db.Column(db.Integer)

    def __init__(self, cpf, data_nascimento, placa, km):
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.placa = placa
        self.km = km


# Rotas


@app.route("/")
def index():
    usuarios_objetos = Usuario.query.all()
    veiculos_objetos = Veiculo.query.all()
    passageiros_objetos = Passageiro.query.all()
    motoristas_objetos = Motorista.query.all()
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template("dashboard.html", usuarios_objetos=usuarios_objetos, veiculos_objetos=veiculos_objetos, passageiros_objetos=passageiros_objetos, motoristas_objetos=motoristas_objetos)

@app.route("/add-user", methods=["GET","POST"])
def addUser():
    if request.method == "POST":
        usuario = Usuario(request.form['nome'], request.form['cpf'], request.form['data_nascimento'], request.form['endereco'], request.form['login'], request.form['senha'])
        db.session.add(usuario)
        db.session.commit()
        return render_template("dashboard.html")
    return render_template("addUser.html")

@app.route("/add-veiculo", methods=["GET","POST"])
def addVehicle():
    if request.method == "POST":
        veiculo = Veiculo(request.form['nome'], request.form['cpf'], request.form['tipo'], request.form['placa'], request.form['marca'], request.form['modelo'], request.form['ano'], request.form['capacidade'])
        db.session.add(veiculo)
        db.session.commit()
        return render_template("dashboard.html")
    return render_template("addVehicle.html")

@app.route("/add-passageiro", methods=["GET","POST"])
def addPassanger():
    if request.method == "POST":
        passageiro = Passageiro(request.form['nome'], request.form['cpf'], request.form['data_nascimento'], request.form['endereco'], request.form['cidade'], request.form['uf'])
        db.session.add(passageiro)
        db.session.commit()
        return render_template("dashboard.html")
    return render_template("addPassanger.html")

@app.route("/add-motorista", methods=["GET","POST"])
def addDriver():
    if request.method == "POST":
        motorista = Motorista(request.form['nome'], request.form['cpf'], request.form['data_nascimento'], request.form['endereco'])
        db.session.add(motorista)
        db.session.commit()
        return render_template("dashboard.html")
    return render_template("addDriver.html")

@app.route("/add-transporte", methods=["GET","POST"])
def transport():
    if request.method == "POST":
        transporte = Transporte(request.form['placa'], request.form['cpf'], request.form['data_nascimento'], request.form['km'])
        db.session.add(transporte)
        db.session.commit()
        return render_template("dashboard.html")
    return render_template("transport.html")

@app.route("/relatorio")
def report():
    relatorios_objetos = Transporte.query.all()
    return render_template("report.html", relatorios_objetos=relatorios_objetos)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=['POST','GET'])
def autenticar():
    if "admin" == request.form['usuario'] and "admin" == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect("/")
    else:
        flash('Usuário ou senha invalida!')
        return redirect("/login")

@app.route("/logout")
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)