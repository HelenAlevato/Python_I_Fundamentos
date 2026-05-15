import os
os.system('cls' if os.name == "nt" else "clear")

lista = []

while True:
    nome = input("Digite um nome: ")
    if not nome in lista:
        lista.append(nome)
    else:
        print("Esse nome já foi adicionado!!!")

    op = input("Deseja incluir outro nome na lista? s / n").lower()
    if op == "n":
        break

busca = input("Digite um nome que queira buscar na lista: ").upper()
if busca in lista:
    print("O nome foi encontrado!")

for i, nome in enumerate(lista):
    print(f"I: {i} / Nome: {nome}")
