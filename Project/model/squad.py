from model.framework import Framework
from model.backend import Backend
from model.sgbd import Sgbd

# classe squad
class Squad:

    # Metodo que inicia sempre que a classe é chamada
    def __init__(self):
        self.ID = 0
        self.NOME = ''
        self.DESCRICAO = ''  
        self.NUMEROPESOSAS = 0 
        self.LINGUAGEMBACKEND = Backend()  
        self.FRAMEWORKFRONTEND = Framework() 
        self.SGBD = Sgbd()

    def __str__(self):
        return f'{self.ID} {self.NOME} {self.DESCRICAO} {self.NUMEROPESOSAS} {self.LINGUAGEMBACKEND} {self.FRAMEWORKFRONTEND}'

