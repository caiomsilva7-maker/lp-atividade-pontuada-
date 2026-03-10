import os
os.system('cls')

cor = input("Digite a cor do CD: ")

if cor.lower() == "verde":
 preco = 10
elif cor.lower() == "azul":
 preco = 20
elif cor.lower() == "amarelo":
 preco = 30
elif cor.lower() == "vermelho":
 preco = 40
else:
 preco = 0
print("Cor inválida")

print("Preço:", preco)