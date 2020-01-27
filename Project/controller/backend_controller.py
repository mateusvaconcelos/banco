# --- imports --- #
from dao.backend_db import BackendDB
from model.backend import Backend

# classe de controle do backend
class BackendController:
    dao = BackendDB()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def criar(self, backend:Backend):
        return self.dao.criar(backend)
        
    def alterar(self, backend:Backend):
        self.dao.alterar(backend)

    def deletar(self, id):
        self.dao.deletar(id)
