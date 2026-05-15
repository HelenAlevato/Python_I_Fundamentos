import os
import random
os.system('cls' if os.name == "nt" else "clear")

pecas = ("pedra", "papel", "tesoura")

computador = random.randint(0,2)
jogador = int(input('''Escolha uma opção 
                [0] - Pedra
                [1] - Papel
                [2] - Tesoura
                '''))

print(f"O computador escolheu: {pecas[computador]}")
print(f"O Jogador escolheu: {pecas[jogador]}")

tabela = ((0,1,-1), (-1,0,-1), (1,-1,0))
jogada = tabela[computador][jogador]

if jogada == 0:
    print("Empate")
elif jogada == 1:
    print("Vence o jogador")
elif jogada == -1:
    print("Vence o computador")