#       ****** MINI CALCULADORA ******

# def somar(a,b):
#     return a + b

# def subtrair(a,b):
#     return a - b

# def dividir(a,b):
#     return a / b

# def multiplicar(a,b):
#     return a * b

# Tudo dentro da função calculadora
def calculadora(a,b,op):
    if op == 1:
        return a + b
    elif op == 2:
        return a - b
    elif op == 3:
        return a * b
    elif op == 4:
        return a / b if b != 0 else "Erro: Divisão por Zero"
    else:
        return "Operação inválida"
    
# Exemplo simplificando o código a cima
def calculadora_up(a,b,op):
    operacoes ={
        1:a+b,
        2:a-b,
        3:a*b,
        4:a/b if b!=0 else "Erro: Divisão por zero"
    }
    return operacoes[op]

#       ****** CADASTRO ALUNOS ******

def add_aluno(lista, nome):
    if nome in lista:
        print("Nome já existe na lista")
    else:
        lista.append(nome.lower())
    
def listar_alunos(lista):
    if len(lista) > 0:
        for nome in lista:
            print(f"nome")
    else:
        print("Lista vazia!!!")

def buscar_aluno(lista, nome):
    if nome.lower() in lista:
        print(f"Existe o nome: {nome} na lista")
    else:
        print(f"Não existe esse nome: {nome} na lista!!!")

def remover_aluno(lista, nome):
    if nome.lower() in lista:
        lista.remove(nome)
    else:
        print("Nome não encontrado!!!")