# --- imports --- #
import MySQLdb
from model.sgbd import Sgbd

# Classe para manipulação da tabela Sgbd
class SgbdDB:
    conexao = MySQLdb.connect(host = 'mysql.padawans.dev', database = 'padawans05', user = 'padawans05', passwd = 'GM2019')
    cursor = conexao.cursor()
    database_table = 'padawans05.Sgbd_FRONTEND'

    def listar_todos(self):
        '''lista todos os elementos do sgbd'''
        # Comando para listar todos no banco de dados
        comando = f'SELECT * FROM {self.database_table};'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # Pega todos os elementos que resultarem da busca
        return resultado

    def buscar_por_id(self, id):
        '''Buscar Sgbd a partir do id'''
        comando = f'SELECT * FROM {self.database_table} WHERE ID = {id}'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def criar(self, sgbd:Sgbd):
        '''cirar sgbd'''
        comando = f'''
        INSERT INTO {self.database_table}
        (
            NOME
        )
        VALUES
        (
            '{sgbd.NOME}',
        );'''
        self.cursor.execute(comando)
        self.conexao.commit()

    def alterar(self, sgbd:Sgbd):
        '''Aterar informações do banco de dados :D'''
        comando = f'''
        UPDATE {self.database_table} SET
        NOME = '{sgbd.NOME}',
        WHERE ID = {sgbd.ID}
        '''

    def deletar(self, id):
        comando = f'DELETE FROM {self.database_table} WHERE ID={id}'
        self.cursor.execute(comando)
        self.conexao.commit()
    