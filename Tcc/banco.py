import sqlite3 as lite
# criando conexão com banco de dados SQL

conexao = lite.connect('dados.db')

class banco_dados():
    with conexao:
        cursor = conexao.cursor()
       
        cursor.execute("CREATE TABLE IF NOT EXISTS usuario(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            nome VARCHAR(250) NOT NULL,\
            telefone BIGINT(25) NOT NULL,\
            email VARCHAR(250) NOT NULL)")

        cursorevent = conexao.cursor()
        cursorevent.execute("CREATE TABLE IF NOT EXISTS evento (\
                evento_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                evento VARCHAR(40) NOT NULL,\
                data date NOT NULL,\
                cidade VARCHAR(40) NOT NULL,\
                estado VARCHAR(40) NOT NULL,\
                local VARCHAR(40) NOT NULL,\
                espaco VARCHAR(40) NOT NULL,\
                tipo VARCHAR(40) NOT NULL,\
                valor BIGINT(40) NOT NULL,\
                descricao VARCHAR(100) NOT NULL)\
                ")

        cursorregister = conexao.cursor()
        cursorregister.execute("CREATE TABLE IF NOT EXISTS agenda (\
                agenda_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                nome_completo VARCHAR(100) NOT NULL,\
                idade smallint (40) NOT NULL,\
                email VARCHAR(100) NOT NULL,\
                evento_id INTEGER NOT NULL,\
                FOREIGN key (evento_id) REFERENCES evento(evento_id))\
                ")