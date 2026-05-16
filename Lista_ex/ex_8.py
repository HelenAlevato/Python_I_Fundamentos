import os
os.system('cls' if os.name=="nt" else "clear")

# Verificação de aprovação
# Desenvolva um programa que:
# Receba uma nota (0 a 10)
# Classifique como:
## Aproveitamento (>=7)
## Recuperação ()

nota = int(input("Qual a nota, entre 0 à 10?"))

while nota < 0 or nota > 10:
    print("Nota invalida")
    nota = int(input("Qual a nota, entre 0 à 10?"))

if nota >=7:
    print("Bom aproveitamento")
else:
    print("recuperacao")

