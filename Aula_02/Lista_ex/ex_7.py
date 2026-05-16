import os
os.system('cls' if os.name=="nt" else "clear")

# Maior entre dois números
# Crie um programa que:
# Receba dois números;
# Mostre qual é o maior ou se são iguais.
# Objetivo: comparação com condicionais.

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))




if numero1 > numero2:
    print("Número 1 é maior")
elif numero1 < numero2:
    print("Número 2 é maior")
elif numero1 == numero2:
    print("Os números são iguais")


