import sqlite3

class Database:
    """Classe que representa o banco de dados (database) da aplicação."""

    def __init__(self, nome='banco.db'):
        self.nome = nome
        self.conexao = None

    def connect(self):
        """Conecta ao banco de dados passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def disconnect(self):
        """Encerra a conexão com o banco de dados"""
        try:
            self.conexao.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para ser encerrada.')

    def createTable(self):
        """Cria tabelas no banco"""
        try:
            cursor = self.conexao.cursor()
            sql = """CREATE TABLE IF NOT EXISTS clients(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL
            );"""
            cursor.execute(sql)
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para criar uma tabela.')
    
    def createNewClient(self, name, cpf, email):
        """Cria um novo registro de cliente no banco"""
        try:
            cursor = self.conexao.cursor()
            sql = """INSERT INTO clients (name, cpf, email) VALUES (?, ?, ?)"""
            try:
                cursor.execute(sql, (name, cpf, email))
            except sqlite3.IntegrityError:
                print(f'Erro: Já existe um cliente cadastrado com o cpf {cpf}.')
            self.conexao.commit()
            print(f'Cliente {name} cadastrado com sucesso.')
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para criar um novo registro de cliente.')
    
    def showClient(self, cpf):
        """Busca um cliente na base da dados"""
        try:
            cursor = self.conexao.cursor()
            sql = """SELECT * FROM clients WHERE cpf = :cpf"""
            cursor.execute(sql, {"cpf": cpf})
            response = cursor.fetchone()
            if response == None:
                print(f'Cliente portador do CPF {cpf} não encontrado')
                return 0
            print(f'Cliente encontrado: \nID -> {response[0]} \nNome -> {response[1]} \nCPF -> {response[2]} \nE-mail -> {response[3]}')
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para buscar um cliente na base de dados.')

    def deleteClient(self, cpf):
        """Remove um cliente da base da dados"""
        try:
            cursor = self.conexao.cursor()
            sql = """DELETE FROM clients WHERE cpf = :cpf"""
            cursor.execute(sql, {"cpf": cpf})
            self.conexao.commit()
            print('Cliente removido da base de dados com sucesso.')
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para remover um cliente da base de dados.')
