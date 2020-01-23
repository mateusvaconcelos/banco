# classe backend
class Backend:

    # Metodo que inicia sempre que a classe é chamada
    def __init__(self):
        self.ID = 0
        self.NOME = ''

    def __str__(self):
        return f'{self.ID} {self.NOME}'