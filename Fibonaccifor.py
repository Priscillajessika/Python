#Iniciar Fibonacci
quantidade = 1


for i in range (start = 1):
    quantidade = int(input("Digite um numero inteiro para o calculo do FIBONACCI: "))
    numero1 = 0
    numero2 = 1

#imprimindo as variaveis iniciais
    print(numero1)
    print(numero2)

#calculando o fibonacci
    for x in range (quantidade): 
        numero3 = numero1 + numero2
        print(numero3)
        numero1 = numero2
        numero2 = numero3
    

