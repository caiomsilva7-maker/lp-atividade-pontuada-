import os
os.system('cls')

nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
estado = input("Digite o estado civil: ")

if sexo == "F" and estado.upper() == "CASADA":
 tempo = input("Quanto tempo de casamento (anos)? ")

print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado)