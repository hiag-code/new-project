import sqlite3 as sql
from this import d

class DataBase:
    def __init__(self, dbPath: str = 'campeonato'):
        self.dbPath = dbPath
        self.conn = None

    def connectar(self):
        """se conectar com o banco de dados"""
        self.conn = sql.connect(self.dbPath)
        self.conn.row_factory = sql.Row
        self.conn.execute("pragma foreign keys = on")
        return self.conn
    
    def fechar(self):
        """fechar conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def cursor(self):
        if self.conn is None:
            self.conectar()
        return self.conn.cursor()
    
    def criarTabelas(self):
        cur = self.cursor()
        cur.execute(
            '''
            create table if not exists categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            );
            '''
        )
        cur.execute(
            '''
            create table if not exists atletas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER CHECK(idade  >= 7 AND idade <= 150) NOT NULL,
            altura REAL,
            peso REAL,
            data_nascimento
            ativo INTEGER DEFAULT 1,
            observacoes TEXT,
            telefone TEXT,
            categoria_id INTEGER NOT NULL,
            momento_cadastro TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
            );
            '''
        )
    def limparDados(self):
        cur = self.cursor()
        cur.execute('DELETE FROM atleta')
        cur.execute('DELETE FROM categoria')
        cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('pessoa', 'categoria');")
