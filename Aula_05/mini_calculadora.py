import os
os.system('cls' if os.name == "nt" else "clear")
import funcoes as fn

# Atividade01 - Mini Calculadora
# O usuário deve:
# escolher opção
# informar dois números
# visualizar resultado

funcoes = int(input('''Escolha uma opção:
                    [1] - soma
                    [2] - subtração
                    [3] - dividir
                    [4] - multiplicar
                    '''))

while True:
    numero1 = int(input("escolha o primeiro número da conta: "))
    numero2 = int(input("escolha o segundo número da conta: "))
    resultado = 0
    if funcoes == 1:
        resultado = fn.somar(numero1,numero2)
    elif funcoes == 2:
        resultado =  fn.subtrair(numero1,numero2)
    elif funcoes == 3:
        resultado =  fn.dividir(numero1,numero2)
    elif funcoes == 4:
        resultado = fn.multiplicar(numero1,numero2)
    else:
        print("Rode novamente o sistema!")

    print(f"Seu resultado é: {resultado}")

    pergunta = input("Deseja fazer outra operação matematica? s / n: ").lower()
    if pergunta == "n":
        break
