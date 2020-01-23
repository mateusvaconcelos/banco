from flask import Flask, render_template, request, redirect
import sys
sys.path.append('C:/Users/900149/Desktop/ideias/AulasPython/36-Aula36')
from Controller.pessoa_controller import PessoaController
from Controller.endereco_controller import EnderecoController
from Model.endereco import Endereco
from Model.pessoa import Pessoa

app = Flask(__name__)
pessoa_controller = PessoaController()
end_controller = EnderecoController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    pessoas = pessoa_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = pessoas)

@app.route('/cadastrar')
def cadastrar():
    pessoa = Pessoa()
    pessoa.endereco = Endereco()
    if 'id' in request.args:
        id = request.args['id']
        pessoa = pessoa_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, pessoa = pessoa )


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    id_end = request.args['id_end']
    pessoa_controller.deletar(id)
    if id_end != 'None':
        end_controller.deletar(id_end)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    pessoa = Pessoa()
    pessoa.id = request.args['id']
    pessoa.nome = request.args['nome']
    pessoa.sobrenome = request.args['sobrenome']
    pessoa.idade = request.args['idade']

    end = Endereco()
    end.id = request.args['endereco_id']
    end.logradouro = request.args['logradouro']
    end.numero = request.args['numero']
    end.complemento = request.args['complemento']
    end.bairro = request.args['bairro']
    end.cidade = request.args['cidade']
    end.cep = request.args['cep']

    pessoa.endereco = end
    if pessoa.id == 0:
        pessoa_controller.salvar(pessoa)
    else:
        pessoa_controller.alterar(pessoa)
    return redirect('/listar')

app.run(debug=True)

