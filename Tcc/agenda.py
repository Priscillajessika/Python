import sqlite3
import sqlite3 as lite

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




