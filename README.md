# Disciplina de Programação WEB


Proposta da Medida de Eficiência:

Seu Francisco está gerenciando um pequeno negócio de transporte de passageiros em sua cidade. Como o
negócio está crescendo, ele pediu sua ajuda para construir um sistema simples de controle com os seguintes
requisitos:

#### • Login (0,2):
o Deverá validar usuário e senha junto ao cadastro do usuário; caso o usuário não exista, deverá
exibir a opção de cadastro;
o Após a realização do login com sucesso, o sistema deverá exibir uma Home com as opções de
menu para acesso as funcionalidades a seguir;

#### • Cadastro de usuário (0,2):
o O cadastro deverá contar com os seguintes campos: Nome, Data de Nascimento, CPF, Endereço,
login, senha;
o O sistema deverá validar se já existe um cadastro para o mesmo CPF;

#### • Cadastro de passageiros (0,2):
o O cadastro deverá contar com os seguintes campos: Nome, Data de Nascimento, CPF, Endereço;
Cidade, UF;
o O sistema deverá validar se já existe um cadastro para o mesmo CPF;
• Cadastro do motorista (0,2);
o O cadastro deverá contar com os seguintes campos: Nome, Data de Nascimento, CPF, Endereço;
o O sistema deverá validar se já existe um cadastro para o mesmo CPF;

#### • Cadastro de veículo (0,2):
o O cadastro deverá contar com os seguintes campos: tipo de transporte (carro, ônibus, VAN), placa,
marca, modelo, ano, capacidade de passageiros, CPF do motorista;
o O sistema deverá validar se já existe um cadastro para a mesma placa;
o O sistema deverá validar se o CPF do motorista informado é válido (se existe no cadastro de
motorista);

#### • Registro do transporte (0,3):
o O registro será o controle dos transportes realizados diariamente pelos veículos e deverá contar
com as seguintes informações: placa do veículo, CPF do passageiro, data do transporte, hora do
transporte, quantidade de KM do trajeto, valor cobrado (calcular R$ 0,40 por KM rodado);
o O sistema deverá validar se o CPF do passageiro informado é válido (se existe no cadastro de
passageiro);
o O sistema deverá validar se a placa do veículo informada é válida (se existe no cadastro de
veículo);

#### • Relatório Financeiro (0,2):
o Apresenta os transportes realizados em um período de data informado pelo usuário;
o Deve haver um filtro de data início e data fim;
o Deve apresentar o valor arrecadado e a quantidade de transportes realizados por tipo de transporte
(carro, ônibus, VAN).
