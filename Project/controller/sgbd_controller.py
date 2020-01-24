# --- imports --- #
from dao.sgbd_db import SgbdDB
from model.sgbd import Sgbd

# classe de controle do sgbd
class SgbdController:
    dao = SgbdDB()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def criar(self, sgbd:Sgbd):
        return self.dao.criar(sgbd)
        
    def alterar(self, sgbd:Sgbd):
        self.dao.alterar(sgbd)

    def deletar(self, id):
        self.dao.deletar(id)
        