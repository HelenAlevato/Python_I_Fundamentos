import os
os.system('cls' if os.name == "nt" else "clear")
import funcoes as fn

# Atividade01 - Mini Calculadora
# O usuário deve:
# escolher opção
# informar dois números
# visualizar resultado

while True:
    numero1 = int(input("escolha o primeiro número da conta: "))
    numero2 = int(input("escolha o segundo número da conta: "))
    op = int(input('''Escolha uma opção:
                    [1] - soma
                    [2] - subtração
                    [3] - dividir
                    [4] - multiplicar
                    [5] - sair
                    '''))
    if op == 5:
        break
    
    resultado = fn.calculadora(numero1, numero2, op)

    print(f"Seu resultado é: {resultado}")

    pergunta = input("Deseja fazer outra operação matematica? s / n: ").lower()
    if pergunta == "n":
        break
