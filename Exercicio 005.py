import os
os.system('cls')

operacao = input("Digite a operação (+, -, * ou /): ")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if operacao == "+":
 resultado = a + b
elif operacao == "-":
 resultado = a - b
elif operacao == "*":
 resultado = a * b
elif operacao == "/":
 resultado = a / b
else:
 print("Operação inválida")
resultado = None

if resultado != None:
 print("Resultado:", resultado)