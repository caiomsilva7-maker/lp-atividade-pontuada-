import os
os.system('cls')

renda = float(input("Digite a renda mensal: "))
emprestimo = float(input("Valor do empréstimo: "))
parcelas = int(input("Número de parcelas: "))

prestacao = emprestimo / parcelas

if emprestimo <= renda * 10 and prestacao <= renda * 0.30:
 print("Empréstimo aprovado")
else:
 print("Empréstimo não aprovado")