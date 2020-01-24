from flask import Flask, render_template, request, redirect
import sys
sys.path.append('C:/Users/900149/Desktop/banco/Project')
from Controller.backend_controller import BackendController
from Controller.framework_controller import FrameworkController
from Controller.sgbd_controller import SgbdController
from Controller.squad_controller import SquadController
from Model.framework import Framework
from Model.backend import Backend
from Model.squad import Squad
from Model.sgbd import Sgbd

app = Flask(__name__)
backend_controller = BackendController()
framework_controller = framework_controller()
sgbd_controller = SgbdController()
squad_controller = SquadController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squads)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    squad.framework = Framework()
    squad.backend = Backend()
    squad.sgbd = Sgbd()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )


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
    squad = Pessoa()
    squad.ID = request.args['ID']
    squad.NOME = request.args['NOME']
    squad.DESCRICAO = request.args['DESCRICAO']
    squad.NUMEROPESOSAS = request.args['NUMEROPESSOAS']

    FRAMEWORK = Framework()
    FRAMEWORK.ID = request.args['ID']
    FRAMEWORK.NOME = request.args['NOME']

    LINGUAGEM = Backend()
    FRAMEWORK.ID = request.args['ID']
    FRAMEWORK.NOME = request.args['NOME']

    SGBD = Sgbd()
    FRAMEWORK.ID = request.args['3ID']
    FRAMEWORK.NOME = request.args['NOME']

    squad.framework = end
    squad.sackend = end1
    squad.sgbd = end2
        if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

app.run(debug=True)

