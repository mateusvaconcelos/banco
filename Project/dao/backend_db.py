import MySQLdb
from model.backend import Backend
Backend
# Classe para manipulação da tabela LINGUAGEM_BACKEND 
class BackendDB:
    conexao = MySQLdb.connect(host = 'mysql.padawans.dev', database = 'padawans05', user = 'padawans05', passwd = 'gm2019')
    cursor = conexao.cursor()
    database_table = 'padawans05.LINGUAGEM_BACKEND'

    def listar_todos(self):
        '''lista todos os elementos do backend'''
        # Comando para listar todos no banco de dados
        comando = f'SELECT * FROM {self.database_table};'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # Pega todos os elementos que resultarem da busca
        return resultado

    def buscar_por_id(self, id):
        '''Buscar Backend a partir do id'''
        comando = f'SELECT * FROM {self.database_table} WHERE ID = {id}'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def criar(self, backend:Backend):
        '''cirar backend'''
        comando = f'''
        INSERT INTO {self.database_table}
        (
            NOME
        )
        VALUES
        (
            '{backend.NOME}',
        );'''
        self.cursor.execute(comando)
        self.conexao.commit()

    def alterar(self, backend:Backend):
        '''Aterar informações do banco de dados :D'''
        comando = f'''
        UPDATE {self.database_table} SET
        NOME = '{backend.NOME}',
        WHERE ID = {backend.ID}
        '''

    def deletar(self, id):
        comando = f'DELETE FROM {self.database_table} WHERE ID={id}'
        self.cursor.execute(comando)
        self.conexao.commit()
    