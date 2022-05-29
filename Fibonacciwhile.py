quantidade = int(input("Digite um numero inteiro para o calculo do FIBONACCI: "))

#Calculou quantas vezes rodou
contador = 1

numero1 = 0
numero2 = 1

#imprimindo as variaveis iniciais
print(numero1)
print(numero2)

#calculando o fibonacci
while (contador <= quantidade): 
    numero3 = numero1 + numero2
    print(numero3)
    numero1 = numero2
    numero2 = numero3
    contador += 1
    

