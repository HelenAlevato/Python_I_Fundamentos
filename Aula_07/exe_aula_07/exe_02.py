import os
os.system('cls' if os.name == "nt" else "clear")
# 2. Lista de compras inteligente
# Faça um programa com:
# •	Uma função adicionar_item(lista, item) 
# •	Uma função remover_item(lista, item) 
# •	Uma função listar_itens(lista) 
# Use uma lista para armazenar os produtos.
# Desafio extra:
# •	Não permitir itens repetidos. 
# •	Ordenar a lista em ordem alfabética.

lista = []
item = ""

def adicionar_item(lista, item):
    if item not in lista:
        lista.append(item)
        print(f"{item} adicionado.")
    else:
        print(f"{item} já está na lista.")

def remover_item(lista, item):
    if item in lista:
        lista.remove(item)
        print(f"item {item} removido")
    else:
        print("item não removido")

def listar_itens(lista):
    lista.sort()

while True:
    item = input("Adicione algo na lista de compras: ")
    adicionar_item(lista, item)
    listar_itens(lista)

    continuar = input("Deseja incluir mais algum item? s / n")
    if continuar.lower() == "n":
        print(f"{lista}")
        break

    print(f"Sua lista de compras tem esses itens: {lista}")

remover_item2 = input("Quer remover algum item? (remove / n remove): ")
if remover_item2.lower() == "remove":
    item_remover = input("Qual item deseja remover? ")
    remover_item(lista, item_remover)
    print(f"Lista atualizada: {lista}")
else:
    print("Nenhum item removido")

print(f"sua lista: {lista}")
