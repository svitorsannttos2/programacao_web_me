from flask import Flask, render_template, request, redirect, session, flash

class Veiculo:
    def __init__(self, nome, tipo, placa, marca, modelo, ano, capacidade, cpf):
        self.nome=nome
        self.tipo=tipo
        self.placa=placa
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.capacidade=capacidade
        self.cpf=cpf

veiculo1 = Veiculo('Uno', 'Carro', 'HMS3045', 'Fiat', '2016', '2015', '4', '86145986520')
veiculo2 = Veiculo('Onix', 'Carro', 'KLH8596', 'Chevrolet', '2020', '2019', '4', '00236585922')
veiculo3 = Veiculo('Sandero', 'Carro', 'PHE9602', 'Renault', '2022', '2022', '4', '95621452864')
veiculos = [veiculo1, veiculo2, veiculo3]

app = Flask(__name__)
app.secret_key = 'web'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Seu Francisco Transportes', veiculos=veiculos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Veiculo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    tipo = request.form['tipo']
    placa = request.form['placa']
    marca = request.form['marca']
    modelo = request.form['modelo']
    ano = request.form['ano']
    capacidade = request.form['capacidade']
    cpf = request.form['cpf']
    veiculo = Veiculo(nome, tipo, placa, marca, modelo, ano, capacidade, cpf)
    veiculos.append(veiculo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'admin' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

app.run(debug=True)