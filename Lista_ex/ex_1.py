import os
os.system('cls' if os.name=="nt" else "clear")

# média de valores
# Desenvolva um programa que receba dois números e calcule a média aritimética entre eles.

numero1 = int(input("primero numero: "))
numero2 = int(input("segundo numero: "))
media = (numero1 + numero2) / 2 
input(f"sua média é: {media}")


