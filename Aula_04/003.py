import os
os.system('cls')

while True:
    print("Loop")

    # o break faz o codigo parar quando chegar na condição que eu escolhi
    # o continue faz o codigo continuar dependendo da condição que passa para ele
    numero = int(input("Digite um numero: "))
    if numero == 10:
        break

for i in range(1,11):
    if i == 5:
        continue
    print(i)