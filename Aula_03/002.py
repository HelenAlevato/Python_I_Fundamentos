import os
os.system('cls')

# Dentro do range da p escolher quantos vazes vai rodar o for e se quer que ele pare em algum momento, tudo separado por virgula
# for i in range(10):
#     print(i)

# Tabuada usando o for

multiplicador = int(input("Digite um número: \n"))

for i in range(1, 11):
    print(f"{multiplicador} x {i} = {multiplicador * i}")

