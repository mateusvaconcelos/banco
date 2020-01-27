# --- imports --- #
from dao.framework_db import FrameworkDB
from model.framework import Framework

# classe de controle do framework
class FrameworkController:
    dao = FrameworkDB()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def criar(self, framework:Framework):
        return self.dao.criar(framework)
        
    def alterar(self, framework:Framework):
        self.dao.alterar(framework)

    def deletar(self, id):
        self.dao.deletar(id)
