import MySQLdb
import sys
sys.path.append('C:/Users/900171/Documents/GITHUB/banco/Project')
from model.squad import Squad
from dao.squad_db import SquadDB

from model.framework import Framework
from controller.framework_controller import FrameworkController

from model.backend import Backend
from controller.backend_controller import BackendController

from model.sgbd import Sgbd
from controller.sgbd_controller import SgbdController

# Controller vai realizar a união do DAO com o MODEL
class SquadController:
    dao = SquadDB()
    framework_controller = FrameworkController()
    backend_controller = BackendController() 
    sgbd_controller = SgbdController()

    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.ID = s[0]
            squad.NOME = s[1]
            squad.DESCRICAO = s[2]
            squad.NUMEROPESOSAS = s[3]

            squad.FRAMEWORKFRONTEND = Framework()
            squad.FRAMEWORKFRONTEND.ID = s[7]
            squad.FRAMEWORKFRONTEND.NOME = s[8]

            squad.LINGUAGEMBACKEND = Backend()
            squad.LINGUAGEMBACKEND.ID = s[9]
            squad.LINGUAGEMBACKEND.NOME = s[10]

            squad.SGBD = Sgbd()
            squad.SGBD.ID = s[12]
            squad.SGBD.NOME = s[13]
            lista_squad.append(squad)

        return lista_squad

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.ID = s[0]
        squad.NOME = s[1]
        squad.DESCRICAO = s[2]
        squad.NUMEROPESOSAS = s[3]

        squad.FRAMEWORKFRONTEND = Framework()
        squad.FRAMEWORKFRONTEND.ID = s[7]
        squad.FRAMEWORKFRONTEND.NOME = s[8]

        squad.LINGUAGEMBACKEND = Backend()
        squad.LINGUAGEMBACKEND.ID = s[9]
        squad.LINGUAGEMBACKEND.NOME = s[10]

        squad.SGBD = Sgbd()
        squad.SGBD.ID = s[12]
        squad.SGBD.NOME = s[13]
        return squad   

    def salvar(self, squad: Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(squad) 

    def deletar(self, id):
        self.dao.deletar(id)
        