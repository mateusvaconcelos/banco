 from model.framework import Framework
from model.backend import Backend
from model.framework import Framework


# classe squad
class Squad:

    # Metodo que inicia sempre que a classe é chamada
    def __init__(self):
        self.ID = 0
        self.NOME = ''
        self.DESCRICAO = ''  
        self.NUMEROPESOSAS = 0 
        self.LINGUAGEMBACKEND = ''  
        self.FRAMEWORKFRONTEND = '' 
        self

    def __str__(self):
        return f'{self.ID} {self.NOME} {self.DESCRICAO} {self.NUMEROPESOSAS} {self.LINGUAGEMBACKEND} {self.FRAMEWORKFRONTEND}'

