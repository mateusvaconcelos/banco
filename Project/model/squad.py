# classe squad
class Squad:

    # Metodo que inicia sempre que a funçãoé chamada
    def __init__(self):
        self.ID = 0
        self.NOME = ''
        self.DESCRICAO = ''  
        self.NUMEROPESOSAS = 0 
        self.LINGUAGEMBACKEND = ''  
        self.FRAMEWORKFRONTEND = '' 

    def __str__(self):
        return f'{self.ID} {self.NOME} {self.DESCRICAO} {self.NUMEROPESOSAS} {self.LINGUAGEMBACKEND} {self.FRAMEWORKFRONTEND}'

