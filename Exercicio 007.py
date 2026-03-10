import os
os.system('cls')

produto = input("Nome do produto: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço unitário: "))

total = quantidade * preco

if quantidade <= 5:
 desconto = total * 0.02
elif quantidade <= 10:
 desconto = total * 0.03
else:
 desconto = total * 0.05

total_pagar = total - desconto

print("Produto:", produto)
print("Total:", total)
print("Desconto:", desconto)
print("Total a pagar:", total_pagar)