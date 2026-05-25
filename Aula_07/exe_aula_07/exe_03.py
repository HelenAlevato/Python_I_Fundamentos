import os
os.system('cls' if os.name == "nt" else "clear")
# 3. Análise de números
# Peça vários números ao usuário e armazene em uma lista.
# Crie funções para:
# •	Retornar o maior número 
# •	Retornar o menor número 
# •	Retornar a média 
# •	Retornar apenas os números pares 
# Exemplo:
# numeros = [4, 7, 10, 3, 8]

numeros = []
numero = ""

# def maior_numero(numeros):

# def menor_numero(numeros):

# def media(numeros):

while True:
    numero = int(input("Adicione um número: "))
    numeros.append(numero)

    continuar = input("Deseja adicionar mais um número na lista? s/n")
    if continuar.lower() == "n":
        break
print(f"{numeros}")
