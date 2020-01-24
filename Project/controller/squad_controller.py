import sys
sys.path.append('C:/Users/900171/Documents/GITHUB/banco/Project')
from model.squad import Squad
from dao.squad_db import SquadDB
import MySQLdb

# Controller vai realizar a união do DAO com o MODEL
class SquadController:
    dao = SquadDB()

    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.ID = s[0]
            squad.NOME = s[1]
            squad.DESCRICAO = s[2]
            squad.NUMEROPESOSAS = s[3]
            squad.LINGUAGEMBACKEND.NOME = s[4]
            squad.FRAMEWORKFRONTEND.NOME = s[5]
            squad.SGBD.NOME = s[6]
            lista_squad.append(squad)

        return lista_squad

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.ID = s[0]
        squad.NOME = s[1]
        squad.DESCRICAO = s[2]
        squad.NUMEROPESOSAS = s[3]
        squad.LINGUAGEMBACKEND.NOME = s[4]
        squad.FRAMEWORKFRONTEND.NOME = s[5]
        squad.SGBD.NOME = s[6]
        return squad   

    def salvar(self, squad: Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(squad) 

    def deletar(self, id):
        self.dao.deletar(id)
