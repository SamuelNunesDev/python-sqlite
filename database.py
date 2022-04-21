import sqlite3
from urllib import response

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
            print('-' * 100)

    def createTable(self):
        """Cria tabelas no banco"""
        try:
            cursor = self.conexao.cursor()
            sql = """CREATE TABLE IF NOT EXISTS clients(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password VARCHAR(20) NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL
            );"""
            cursor.execute(sql)
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para criar uma tabela.')
            print('-' * 100)
    
    def createNewClient(self, name, cpf, senha, email):
        """Cria um novo registro de cliente no banco"""
        try:
            cursor = self.conexao.cursor()
            sql = """INSERT INTO clients (name, password, cpf, email) VALUES (?, ?, ?, ?)"""
            try:
                cursor.execute(sql, (name, cpf, senha, email))
            except sqlite3.IntegrityError:
                print(f'Erro: Já existe um cliente cadastrado com o cpf {cpf}.')
                print('-' * 100)
            self.conexao.commit()
            print(f'Cliente {name} cadastrado com sucesso.')
            print('-' * 100)
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para criar um novo registro de cliente.')
            print('-' * 100)
    
    def showClient(self, cpf):
        """Busca um cliente na base da dados"""
        try:
            cursor = self.conexao.cursor()
            sql = """SELECT id, name, cpf, email FROM clients WHERE cpf = :cpf"""
            cursor.execute(sql, {"cpf": cpf})
            response = cursor.fetchone()
            if response == None:
                print(f'Cliente portador do CPF {cpf} não encontrado')
                print('-' * 100)
                return 0
            print(f'Cliente encontrado: \nID -> {response[0]} \nNome -> {response[1]} \nCPF -> {response[2]} \nE-mail -> {response[3]}')
            print('-' * 100)
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para buscar um cliente na base de dados.')
            print('-' * 100)

    def deleteClient(self, cpf):
        """Remove um cliente da base da dados"""
        try:
            cursor = self.conexao.cursor()
            sql = """DELETE FROM clients WHERE cpf = :cpf"""
            cursor.execute(sql, {"cpf": cpf})
            self.conexao.commit()
            print('Cliente removido da base de dados com sucesso.')
            print('-' * 100)
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para remover um cliente da base de dados.')
            print('-' * 100)

    def showClientByEmail(self, email):
        """Busca um cliente na base de dados a partir do email"""
        try:
            cursor = self.conexao.cursor()
            sql = """SELECT id, name, cpf, email FROM clients WHERE email = :email"""
            cursor.execute(sql, {"email": email})
            response = cursor.fetchone()
            if response == None:
                print(f'Cliente portador do e-mail {email} não encontrado')
                print('-' * 100)
                return 0
            print(f'Cliente encontrado: \nID -> {response[0]} \nNome -> {response[1]} \nCPF -> {response[2]} \nE-mail -> {response[3]}')
            print('-' * 100)
            cursor.close()
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para buscar um cliente na base de dados.')
            print('-' * 100)

    def login(self, email, password):
        try:
            cursor = self.conexao.cursor()
            sql = """SELECT * FROM clients WHERE email = ? AND password = ?"""
            cursor.execute(sql, [email, password])
            response = cursor.fetchone()
            if response == None:
                print('Erro ao tentar login, credenciais incorretas.')
                print('-' * 100)
                return 0
            print('Login efetuado com sucesso.')
            print('-' * 100)
            return 1
        except AttributeError:
            print('Erro: Não existe uma conexão ativa para buscar um cliente na base de dados.')
            print('-' * 100)
