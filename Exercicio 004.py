import os
os.system('cls')

morango = float(input("Quantos kg de morango: "))
maca = float(input("Quantos kg de maca: "))

if morango <= 5:
 preco_morango = morango * 2.50
else:
 preco_morango = morango * 2.20

if maca <= 5:
 preco_maca = maca * 1.80
else:
 preco_maca = maca * 1.50

total = preco_morango + preco_maca
kg = morango + maca

if kg > 10 or total > 15:
 desconto = total * 0.10
total = total - desconto

print("Valor a pagar:", total)