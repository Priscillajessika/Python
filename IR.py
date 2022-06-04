salario = float(input("Digite o seu salario: ")) 
#Validação de salário

if(salario >= 1903.99 and salario <=2826.85):
    valorir = salario * 0.075 
    salarioliq = salario - valorir
    print("Salario menos 7.5% de IR R$" ,salarioliq)

elif(salario >= 2826.66 and salario <=3751.05):
    valorir = salario * 0.15 
    salarioliq = salario - valorir
    print("Salario menos 15% de IR R$" ,salarioliq)

elif(salario >= 3751.06 and salario <=4664.68):
    valorir = salario * 0.225 
    salarioliq = salario - valorir
    print("Salario menos 22.5% de IR R$" ,salarioliq)   

elif(salario > 4664.68):
    valorir = salario * 0.275
    salarioliq = salario - valorir
    print("Salario menos 27.5% de IR R$" ,salarioliq) 

else:
    print("Salario isento de IR R$" ,salario)