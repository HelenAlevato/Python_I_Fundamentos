import os
import funcoes as fn # Importa o arquivo funções e apelida ele de fn

os.system('cls' if os.name=="nt" else 'clear') # cls para nome nt se não para nome clear, dependendo do sistema operacional de cada pessoa

# A caixa de ferramentas tem a função "somar" dentro
resultado = fn.somar(5,2) # Usa a função do arquivo somar
print(resultado)