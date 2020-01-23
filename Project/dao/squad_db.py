# --- imports --- #
import MySQLdb
from model.squad import Squad

# Classe de squads
class SquadDB:
    conexao = MySQLdb.connect(host = 'localhost', database = 'squads', user = 'root', passwd = '')
    cursor = conexao.cursor()
    database_table = 'squads.squads'

    def listar_todos(self):
        # Criação do comando para pegar todos os elementos da tabela
        comando = f'SELECT * FROM {self.database_table}'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # Vai pegar todos os elementos da tabela
        return resultado

    def buscar_por_id(self, ID):
        '''Buscar squad a partir do ID'''
        comando = f'SELECT * FROM {self.database_table} WHERE ID = {ID}'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        '''Salvar Squad'''
        comando = f'''
        INSERT INTO {self.database_table}
        (
            NOME,
            DESCRICAO,
            NUMEROPESSOA,
            LINGUAGEMBACKEND,
            FRAMEWORKFRONT
        )
        VALUES
        (
            '{squad.NOME}',
            '{squad.DESCRICAO}',
            {squad.NUMEROPESOSAS},
            '{squad.LINGUAGEMBACKEND}',
            '{squad.FRAMEWORKFRONTEND}'
        );'''
        self.cursor.execute(comando)
        self.conexao.commit()

    def alterar(self, squad:Squad):
        
        '''Aterar informações do banco de dados :D'''
        comando = f'''
        UPDATE {self.database_table} SET
        NOME = '{squad.NOME}',
        DESCRICAO = '{squad.DESCRICAO}',
        NUMEROPESSOA = {squad.NUMEROPESOSAS},
        LINGUAGEMBACKEND = '{squad.LINGUAGEMBACKEND}',
        FRAMEWORKFRONT = '{squad.FRAMEWORKFRONTEND}'
        WHERE ID = {squad.ID}
        '''
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f'DELETE FROM {self.database_table} WHERE ID={id}'
        self.cursor.execute(comando)
        self.conexao.commit()

    