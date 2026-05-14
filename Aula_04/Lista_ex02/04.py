import os
os.system('cls')

# 4. Mostrar apenas pares 
# Mostre todos os números pares entre 1 e 100 usando range. 

numeros_pares = 0

# 2 → valor inicial.
# 101 → valor final não incluso (o range para antes de chegar nele).
# 2 → passo (incremento), ou seja, pula de 2 em 2.

for i in range(2,101,2):
    print(i)


for i in range(1,101):
    if i % 2 == 0:
        print(i)

for i in range(1,101):
    if i % 2 == 0:
        continue
    print(i)