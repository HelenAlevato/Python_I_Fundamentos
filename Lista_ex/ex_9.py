import os
os.system('cls' if os.name=="nt" else "clear")

# Calculadora simples
# Crie um programa que:
# •	Receba dois números 
# •	Receba uma operação (+, -, *, /) 
# •	Execute a operação escolhida 
# Objetivo: múltiplas condições com if, elif, else.

numero1 = int(input("Primeiro numero: "))
numero2 = int(input("Segundo numero: "))

operacao = input("Qual operacao quer fazer? ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "/":
    resultado = numero1 / numero2
elif operacao == "*":
    resultado = numero1 * numero2
else:
    print("Digite uma opcao valida")

print (f"Resultado: {resultado}")