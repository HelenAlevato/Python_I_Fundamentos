import os
os.system('cls' if os.name=="nt" else "clear")

# operações básicas
# Crie um programa que receba dois números e mostre o resultado da: soma, subtração, multiplicação e divisão

numero1 = int(input("número 1: "))
numero2 = int(input("número 2: "))

operacao = (input("escolha o operador: "))

if operacao == "+":
    resultado = numero1 + numero2 
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Digite uma opção válida!")

print (f"Resultado: {resultado}")