from re import I

# Lista vazia para palavras do arquivo palavras
lista_palavras = []

# Abrindo o arquivo palavras, lendo o arquivo e adicionando cada palavra na lista palavras
with open('Palavras.txt', 'r' , encoding='utf-8' ) as arquivo:
    for palavra in arquivo:
        lista_palavras.append(palavra.upper())

# Função
def contar_palavras(lista_palavras):
    # Contando as palavras         
    return len(lista_palavras)

quantidade = contar_palavras(lista_palavras)
print(f"A lista contem {quantidade}, palavras.")

# Função
def contarletras_do_alfabeto(lista_palavras):
    # Contando quantas vezes cada letra do alfabeto tem na lista
    dicionario_letras = {}
    # A = 123
    # B = 321
    # ...
    for palavra in lista_palavras:
        # palavra = 'PRISCILLA'
        lista_letras = list(palavra)
        # lista_letras = ['P','R','I','S','C','I','L','L','A']
        for letra in lista_letras:
            # letra = 'P'
            if letra not in dicionario_letras:
                dicionario_letras[letra] = 1
                # dicionario_letras {
                # 'P':1
                # }
            else:
                dicionario_letras[letra] += 1
                # dicionario_letras {
                # 'P':2
                # }
    return dicionario_letras

contagem_letras = contarletras_do_alfabeto(lista_palavras) 
print("A quantidade de cada letra é:") 
print (contagem_letras)

# Função
def contarletras_inicial(lista_palavras):
    # Contando as letras iniciais
    dicionario_letrasinicias = {}
  
    for palavra in lista_palavras:
        # palavra = 'PRISCILLA'
        # letra = 'P'
            if palavra[0] not in dicionario_letrasinicias:
                dicionario_letrasinicias[palavra[0]] = 1
            else:
                dicionario_letrasinicias[palavra[0]] += 1
            
    return dicionario_letrasinicias

contagem_letrasiniciais = contarletras_inicial(lista_palavras) 
print("A quantidade acumulada de cada letra é:") 
print (contagem_letrasiniciais)