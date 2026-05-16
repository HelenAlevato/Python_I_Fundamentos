import os
os.system('cls')

# Multi tabuada
# o :>4 ocupa 4 casas por exemplo

# for i in range(1,11):
#     print(f"{i:>4}{i*2:>4}{i*3:>4}{i*4:>4}{i*5:>4}{i*6:>4}{i*7:>4}{i*8:>4}{i*9:>4}{i*10:>4}")


for i in range(1,11):
    linha = f"{i:>4}"
    for ii in range(2,11):
        linha += f"{ii*i:>4}"
    print(linha)