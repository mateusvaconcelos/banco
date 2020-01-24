# --- imports --- #
import MySQLdb
from model.squad import Squad

# Classe de squads
class SquadDB:
    conexao = MySQLdb.connect(host = 'mysql.padawans.dev', database = 'padawans05', user = 'padawans05', passwd = 'gm2019')
    cursor = conexao.cursor()
    database_table = 'padawans05.squads'

    def listar_todos(self):
        # Criação do comando para pegar todos os elementos da tabela
        comando = f'SELECT * FROM {self.database_table};'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # Vai pegar todos os elementos da tabela
        print(resultado)
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
            NUMEROPESSOAS
            ID_FRAMEWORK,
            ID_LINGUAGEM,
            ID_SGBD  
        )
        VALUES
        (
            '{squad.NOME}',
            '{squad.DESCRICAO}',
            {squad.NUMEROPESOSAS},
            '{squad.FRAMEWORKFRONTEND.ID}',
            '{squad.LINGUAGEMBACKEND.ID }',
            '{squad.SGBD.ID}'
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


ok = SquadDB()
print(ok.listar_todos())
