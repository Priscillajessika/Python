import os
from pydoc import describe
import sqlite3
import sqlite3 as lite
from sqlite3 import Error
#from termios import VSTART
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

from anyio import open_cancel_scope

####### criando conexao com banco de dados ##########
def ConexaoBanco():

    con = lite.connect('dados.db')

    return con

vcon=ConexaoBanco()

def query(conexao,sql):
    try: 
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operacao concluida.")
        #conexao.close()

def consultar(conexao, sql):
    conexao = ConexaoBanco()
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    #conexao.close()

    return resultado

def menuprincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def inserirmenu():
    os.system("cls")        #Variavel (Nome, telefone e e-mail)
    vnome=input("Digite o nome: ")
    vtelefone=input("Digite o telefone: ")
    vemail=input("Digite o email: ")
    vsql="Insert into 'dados.db' (nome, telefone, email) VALUES ('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    query(vcon,vsql)

def deletarmanu():
    os.system("cls")
    vid=input("Digite o ID do resgitro a ser deletado: ")
    vsql="Delete FROM 'dados.db' WHERE evento_id="+vid
    query(vcon,vsql)

def atualizarmenu():
    os.system("cls")
    vid=input("Digite o ID do registro a ser alterado: ")
    r=consultar(vcon,"SELECT * FROM 'dados.db' WHERE evento_id="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    vnome=input("Digite o nome: ")
    vtelefone=input("Digite o telefone: ")
    vemail=input("Digite o email: ")
    if(len(vnome)==0):
        vnome=rnome
    if(len(vtelefone)==0):
        vtelefone=rtelefone
    if(len(vemail)==0):
        vemail=remail
    vsql="UPDATE 'dados.db' SET nome='"+vnome+"', telefone='"+vtelefone+"', email='"+vemail+"' WHERE evento_id="+vid
    query(vcon,vsql)

def consultartabela(conexao, sql):
    conexao = ConexaoBanco()
    c=conexao.cursor()
    c.execute(sql)
    
    vsql="SELECT * FROM 'dados.db'"
    resultado=consultartabela(vcon,vsql)
    vlimite=10
    vcont=10
    for r in resultado: 
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email: {3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1;
        if(vcont>=vlimite):
            vcont=0
            os.system("pause")
            os.system.clear("cls")
    print("Fim da lista")
    os.system("pause")

def consultarnomes():
    vnome=input("Digite o nome: ")
    vsql="SELECT * FROM 'dados.db' WHERE nome LIKE '%"+vnome+"%'"
    resultado=consultarnomes(vcon,vsql)
    vlimite=10
    vcont=10
    for r in resultado: 
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email: {3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1;
        if(vcont>=vlimite):
            vcont=0
            os.system("pause")
            os.system.clear("cls")
    print("Fim da lista")
    os.system("pause")

opcao=0
while opcao !=6:
    menuprincipal()
    opcao=int(input("Digite uma opcao: "))
    if opcao==1:
        inserirmenu()
    elif opcao==2:
        deletarmanu()
    elif opcao==3:
        atualizarmenu()
    elif opcao==4:
        consultartabela()
    elif opcao==5:
        consultarnomes()
    elif opcao==6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("opcao invalida")
        os.system("pause")

vcon.close()
os.system("pause")
