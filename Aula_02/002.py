import os
os.system('cls' if os.name=="nt" else "clear")

centimetros = float(input("Digite o valor em cm: "))

# polegadas, pes, jardas
opcao = input(" 1 - polegadas \n 2 - Pés \n 3 - Jardas \n Digite aqui a opção correta: ")
print("Escolha uma opção para conversão: ")

if opcao == "1":
    resultado = centimetros / 2.54
elif opcao == "2":
    resultado = centimetros / 30.48
elif opcao == "3":
    resultado = centimetros / 91.44
else:
    print("Digite uma opção válida")

print(f"Resultado = {resultado}")