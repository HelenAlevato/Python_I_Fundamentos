import os
os.system('cls' if os.name=="nt" else "clear")

# Número positivo, negativo ou zero. Crie um programa que:
# Leia um número
# Informe se ele é: positivo, negativo, zero.
# Uso de if, elif e else.

numero = int(input("Coloque um número: "))

valor = input("O que esse número é?: ")

if valor == "positivo":
    resultado = numero >0
elif valor == "negativo":
    resultado = numero <0
elif valor == "zero":
    resultado = numero == 0
else: 
    print("Coloque um valor valido!")

print(f"Seu número é: {resultado}")