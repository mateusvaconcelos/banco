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
        comando = f'''
        SELECT * from {database_table} as s 
        left join padawans05.FRAMEWORK_FRONTEND as ff on s.ID_FRAMEWORK = ff.ID
        left join padawans05.LINGUAGEM_BACKEND as lb on s.ID_FRAMEWORK = lb.ID
        left join padawans05.SGBD as db on s.ID_FRAMEWORK = db.ID;
        '''
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # Vai pegar todos os elementos da tabela
        return resultado

    def buscar_por_id(self, ID):
        '''Buscar squad a partir do ID'''
        comando = f'''
        SELECT * from {database_table} as s 
        left join padawans05.FRAMEWORK_FRONTEND as ff on s.ID_FRAMEWORK = ff.ID
        left join padawans05.LINGUAGEM_BACKEND as lb on s.ID_FRAMEWORK = lb.ID
        left join padawans05.SGBD as db on s.ID_FRAMEWORK = db.ID
        WHERE s.ID = {ID};
        '''
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
