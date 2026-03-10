import os
os.system('cls')

litros = float(input("Litros: "))
tipo = input("Combustível (A ou G): ")

if tipo == "A":
 preco = 3.79
if litros <= 25:
 desconto = 0.02
else:
 desconto = 0.04

if tipo == "G":
 preco = 6.59
if litros <= 25:
 desconto = 0.03
else:
 desconto = 0.05

total = litros * preco
total = total - (total * desconto)

print("Valor a pagar:", total)


