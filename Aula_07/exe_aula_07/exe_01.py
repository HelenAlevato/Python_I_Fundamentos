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


# for com os inputs dos dados
for alunos in sequence:
    nome = input("Qual o nome do aluno? ")
    nota1 = int(input("Primeira nota: "))
    nota2 = int(input("Segunda nota: "))
    nota3 = int(input("Terceira nota: "))
    nota4 = int(input("Quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"{nome} e {media}")
    
# situacao = ""
# if situacao == media =< 6:
#     situacao = "Reprovado"
# elif situacao == media >= 7:
#     situacao == "Aprovado"
# else:
#     print("Digite uma opção valida!")

# objetos de array

# cadastrar_alunos {
#     [
#         nome: nome,
#         media: media,
#         situacao: ""
#     ]
# }

# tratativa de erros imprimir