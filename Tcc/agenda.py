import sqlite3
import sqlite3 as lite
# criando conexão com banco de dados SQL

conexao = lite.connect('dados.db')

class banco_dados():
    with conexao:
    #nome, logradouro, num, bairro, cep, cidade, estado, idade, genero, telefone, cpf, email

        cursor = conexao.cursor()
        #nome, logradouro, num, bairro, cep, cidade, estado, idade, genero, telefone, cpf, email
        cursor.execute("CREATE TABLE IF NOT EXISTS usuario(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            nome VARCHAR(250) NOT NULL,\
            logradouro VARCHAR(250) NOT NULL,\
            num smallint(15) NOT NULL,\
            bairro VARCHAR(100) NOT NULL,\
            cep BIGINT(25) NOT NULL,\
            cidade VARCHAR(100) NOT NULL,\
            estado VARCHAR(50) NOT NULL,\
            idade smallint (10) NOT NULL,\
            genero VARCHAR(250) NOT NULL,\
            telefone BIGINT(25) NOT NULL,\
            cpf BIGINT(14) UNIQUE NOT NULL,\
            email VARCHAR(250) NOT NULL)")

        cursorevent = conexao.cursor()
        cursorevent.execute("CREATE TABLE IF NOT EXISTS evento (\
                evento_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                evento VARCHAR(40) NOT NULL,\
                data date NOT NULL,\
                cidade VARCHAR(40) NOT NULL,\
                estado VARCHAR(40) NOT NULL,\
                local VARCHAR(40) NOT NULL,\
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

            

conexao = lite.connect('dados.db')
cursor = conexao.cursor()

def inserir(evento, data, cidade, estado, local, valor, descricao):
    return """INSERT INTO evento\
             (evento, data, cidade, estado, local, valor, descricao)\
                  VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(evento, data, cidade, estado, local, valor, descricao)

def atualizar(id, evento, data, cidade, estado, local, valor, descricao):  
     return """UPDATE evento 
 SET evento = '{}', data = '{}', cidade = '{}', estado = '{}', local = '{}', valor = '{}', descricao = '{}' 
    where evento_id ='{}'
 """.format(evento, data, cidade, estado, local, valor, descricao, id)
 
 
def deletar(id):
    return """
    DELETE FROM evento WHERE evento_id='{}'
    """.format(id)
   
def exibir():
    cursor.execute("""SELECT * FROM  evento""")
    dados = cursor.fetchall()
    for linha in dados:
        print(linha)

def pergunta():
    Evento = input("\nO que você deseja fazer:\n1 - Criar Evento\n2 - Atualizar Evento\n3 - Deletar Evento\n4 - Exibir Eventos\n0 - Encerrar\n")
    return Evento

Evento = pergunta()

while True:

    if Evento == "1":
        evento=input("Informe do evento: ")
        data=input("Informe a Data do evento: ")
        cidade=input("Informe a Cidade do evento: ")
        estado=input("Informe o Estado do evento: ")
        local=input("Informe o Local do evento: ")
        valor=input("Informe o Valor do ingresso: ")
        descricao=input("Descrição do evento: ")
        cursor.execute(inserir(evento, data, cidade, estado, local, valor, descricao))
        conexao.commit()
              
        
    
        
    elif Evento == "2":
        exibir()
        id=input("\nInforme o Numero do evento que deseja atualizar: ")
        evento=input("Informe do evento: ")
        data=input("Informe a Data do evento: ")
        cidade=input("Informe a Cidade do evento: ")
        estado=input("Informe o Estado do evento: ")
        local=input("Informe o Local do evento: ")
        valor=input("Informe o Valor do ingresso: ")
        descricao=input("Descrição do evento: ")
        cursor.execute(atualizar(id,evento, data, cidade, estado, local, valor, descricao))
        conexao.commit()
        
        print("\nEvento atualizado, segue lista atualizada.\n")
        exibir()
       
        
    elif Evento == "3":
        exibir()
        
        id=input("\nInforme o Numero do evento que deseja deletar: ")
        cursor.execute(deletar(id))
        conexao.commit()
        
        
        print("\nEvento deletado, segue lista atualizada.\n")
        exibir()
        
        
    elif Evento == "4":    
        exibir()
        
    else:
        conexao.close()
        break
        
    
    Evento = pergunta()




