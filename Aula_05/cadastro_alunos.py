import os
os.system('cls' if os.name == "nt" else "clear")
import funcoes as fn

lista_alunos = []
while True:
    escolha = input('''Escolha uma opção:
                    [1] Adicionar alunos
                    [2] Listar alunos
                    [3] Buscar alunos
                    [4] Remover alunos
                    [5] Sair
                    ''' )
    
    if escolha > 0 and escolha < 6:
        if escolha == 1:
            nome = input("Digite um nome:")
            fn.add_aluno(lista_alunos,nome)
        elif escolha == 2:
            fn.listar_alunos(lista_alunos)
        elif escolha == 3:
            fn.buscar_alunos(lista_alunos,nome)
        elif escolha == 4:
            fn.remover_alunos(lista_alunos,nome)
        elif escolha == 5:
            break
    else:
        print("Opção inválida!!!")