import os
os.system('cls' if os.name == "nt" else "clear")
# 1. Cadastro de alunos
# Crie um programa que:
# •	Tenha uma função cadastrar_alunos(nome, nota1, nota2, nota3, nota4) 
# •	Armazene os dados em uma lista no formato:
# ("Maria", 8.0, 7.5)
# •	Depois mostre: 
# o	nome 
# o	média 
# o	situação (“Aprovado” ou “Reprovado”) 
# Exemplo esperado:
# Maria - Média: 7.75 - Aprovado


sala_de_aula = []

def cadastrar_alunos(nome, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # situacao = "Aprovado" if media >= 7 else "Reprovado"
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    aluno = (nome, media, situacao)
    sala_de_aula.append(aluno)

# quantidade de alunos
quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nAluno {i+1}")

    nome = input("Qual o nome do aluno? ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    nota4 = float(input("Quarta nota: "))

    cadastrar_alunos(nome, nota1, nota2, nota3, nota4)

print("\n--- RESULTADO ---")

for aluno in sala_de_aula:
    print(f"{aluno[0]} - Média: {aluno[1]:.2f} - {aluno[2]}")