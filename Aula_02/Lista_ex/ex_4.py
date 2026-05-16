import os
os.system('cls' if os.name=="nt" else "clear")

# Dobro, triplo e quadrado
# Crie um programa que receba um número e exiba:
# - seu dobro
# - seu triplo
# - seu valor ao quadrado

numero = int(input("Qual seu número?: "))
operacao = input("Escolha qual operacao: ")

if operacao == "Dobro":
    valor = numero * 2
elif operacao == "Triplo":
    valor = numero * 3
elif operacao == "Quadruplo":
    valor = numero * 4
else:
    print("Coloque um valor valido!")


print (f"Resultado: {valor}")