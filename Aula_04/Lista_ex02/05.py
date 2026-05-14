import os
os.system('cls')

# 5. Soma dos Dígitos 
# Crie um programa que leia um número inteiro positivo e calcule a soma de todos os seus dígitos. 

numero = int(input("Digite um número: ")) 
soma = 0
while numero > 0:
    soma += numero % 10 # 3521 % 10 = 1 (352,1)
    numero = numero // 10 # 3521 // 10 - 352,1 = 352
    print("numero valido")

print(soma)
