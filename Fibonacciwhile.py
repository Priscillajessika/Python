
#Iniciar Fibonacci
quantidade = 1

while (quantidade > 0):
    quantidade = int(input("Digite um numero inteiro para o calculo do FIBONACCI: ")) 

    contador = 1
    numero1 = 0
    numero2 = 1

#calculando o fibonacci
    while (contador <= quantidade): 
        print(numero1)
        #print(numero2)
        numero3 = numero1 + numero2
        print(numero3)
        numero1 = numero2
        numero2 = numero3
        contador += 1
    

