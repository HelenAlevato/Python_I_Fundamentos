import os
os.system('cls')

# 6. Soma até parar 
# Peça números ao usuário continuamente. 
# O programa deve parar quando o usuário digitar 0. 
# Depois mostre: 
# soma total  
# quantidade de números digitados  

soma = 0
digitados = 0
while True:
    print("Loop")
    numero = int(input("Qual um número?: "))
    # soma += numero
    soma = soma + numero
    digitados += 1
    if numero == 0:
        digitados -= 1 # para nao considerar o 0
        break

print(f"Soma total {soma}")
print(f"Quantidade de números digitados {digitados}")