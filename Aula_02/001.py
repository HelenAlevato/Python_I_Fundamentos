import os
os.system('cls' if os.name=="nt" else "clear")

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("é par")
else: 
    print("é impar")