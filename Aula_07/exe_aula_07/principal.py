import os
from funcoes import*

def exe01():
    try:
        lista_alunos = []
        quanti_alunos = int(input("Quantos alunos quer cadastrar?"))
        for i in range(quanti_alunos):
            nome = input("Digite o nome do aluno: ")
            n1 = float(input("Digite a 1ª Nota: "))
            n2 = float(input("Digite a 2ª Nota: "))
            n3 = float(input("Digite a 3ª Nota: "))
            n4 = float(input("Digite a 4ª Nota: "))
            aluno = cadastrar_alunos(nome,n1,n2,n3,n4)
            if aluno:
                lista_alunos.append(aluno)

        for aluno in lista_alunos:
             print(f"Nome = {aluno[0]} - Média = {aluno[1]:.2f} - Situação = {aluno[2]}")

    except Exception as erro:
        print(f"Erro = {erro}")  


def exe02():
    lista = []
    try:

        while True:
            opcao = input('''
            [1] - Add produto
            [2] - Remover produto   
            [3] - Listar produtos
            [4] - Sair           
            ''')
            if opcao == "1":
                produto = input("Digite o produto: ")
                adicionar_item(lista,produto)
            elif opcao == "2":
                produto = input("Digite o produto: ")
                remover_item(lista,produto) 
            elif opcao == "3":           
                listar_itens(lista) 
            elif opcao == "4":
                break        
            else:
                print("Digite uma opção valida")    
        print("Exercicio 2 finalizado")        
        
    except Exception as erro:
        print(erro)

exe02()    