import os
os.system('cls' if os.name=="nt" else "clear")

# Área do retângulo
# Crie um programa que solicite a base e a altura de um retângulo e calcule: A = base * altura

base = int(input("Valor da base: "))
altura = int(input("Valor da altura: "))

calculo = base * altura

print(f"Resultado: {calculo}")