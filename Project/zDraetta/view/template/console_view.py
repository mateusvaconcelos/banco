import sys
sys.path.append('c:/Users/900171/Documents/GITHUB/python_exercises/Aula037')

import os
from controller.squad_controller import SquadController
from model.squad import Squad

while True:
    print('''
**************************
1 - Listar todos
2 - Buscar por id
3 - Salvar (not working)
4 - Alterar
5 - Deletar
6 - SAIR
**************************
    ''')
    choice = int(input('>> '))

    squad = SquadController()
    if choice == 1:
        # listar todos
        for i in squad.listar_todos():
            print(i)

    if choice == 2:
        id = int(input('Digite o ID\n>>'))
        teste = str(squad.buscar_por_id(id))
        print(teste)

    if choice == 3:
        squad_ = Squad()
        squad_.NOME = input('Digite o nome do squad: ')
        squad_.DESCRICAO = input('DIgite uma descricao para o squad: ')
        squad_.NUMEROPESOSAS = int(input('Digite o numero de pessoas: '))
        squad_.LINGUAGEMBACKEND = input('Dgite qual linguagem foi usada: ')
        squad_.FRAMEWORKFRONTEND = input('Digite qual famework o squad usa: ')
        squad.salvar(squad_)

    if choice == 4:
        squad_ = Squad()
        for i in squad.listar_todos():
            print(i)
        id = int(input('\nDigite o id que se deseja alterar\n>>'))
        squad_.ID = id
        squad_.NOME = input('Digite o nome do squad: ')
        squad_.DESCRICAO = input('DIgite uma descricao para o squad: ')
        squad_.NUMEROPESOSAS = int(input('Digite o numero de pessoas: '))
        squad_.LINGUAGEMBACKEND = input('Dgite qual linguagem foi usada: ')
        squad_.FRAMEWORKFRONTEND = input('Digite qual famework o squad usa: ')
        squad.alterar(squad_)

    if choice == 5:
        print('Digite o id do que se deseja deletar: ')
        id = int(input('>>'))
        squad.deletar(id)

    if choice == 6:
        break

    input('\nPressione enter para continuar ...')
    os.system('cls')