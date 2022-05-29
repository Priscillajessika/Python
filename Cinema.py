#Criar uma lista de lugares

sala = []
fileiras = ["A, ""B, ""C, ""D, ""E, ""F, ""G, ""H, ""I, ""J "]

lugaresquantidades = int(input("Quantidade de lugares: ") )

print(fileiras)

for i in range(lugaresquantidades):
    sala.append(i+1)
    
print("",sala)

poltronare = int(input("Reserve a sua poltrona: ") )-1
sala[poltronare] = ("*")

print(fileiras)   
print(sala)