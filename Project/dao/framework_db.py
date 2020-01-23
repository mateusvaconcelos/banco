# --- imports --- #
import MySQLdb
from model.framework import Framework

# Classe para manipulação da tabela FRAMEWORK_FRONTEND 
class FrameworkDB:
    conexao = MySQLdb.connect(host = 'mysql.padawans.dev', database = 'padawans05', user = 'padawans05', passwd = 'GM2019')
    cursor = conexao.cursor()
    database_table = 'padawans05.FRAMEWORK_FRONTEND'

    def listar_todos(self):
        '''lista todos os elementos do framework'''
        # Comando para listar todos no banco de dados
        comando = f'SELECT * FROM {self.database_table};'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # Pega todos os elementos que resultarem da busca
        return resultado

    def buscar_por_id(self, id):
        '''Buscar Framework a partir do id'''
        comando = f'SELECT * FROM {self.database_table} WHERE ID = {id}'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def criar(self, framework:Framework):
        '''cirar framework'''
        comando = f'''
        INSERT INTO {self.database_table}
        (
            NOME
        )
        VALUES
        (
            '{framework.NOME}',
        );'''
        self.cursor.execute(comando)
        self.conexao.commit()

    def alterar(self, framework:Framework):
        '''Aterar informações do banco de dados :D'''
        comando = f'''
        UPDATE {self.database_table} SET
        NOME = '{framework.NOME}',
        WHERE ID = {framework.ID}
        '''

    def deletar(self, id):
        comando = f'DELETE FROM {self.database_table} WHERE ID={id}'
        self.cursor.execute(comando)
        self.conexao.commit()
    