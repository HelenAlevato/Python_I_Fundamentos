import os
os.system('cls' if os.name=="nt" else "clear")

# Área de um círculo
# Defina a constante PI=3,14.
# Peça ao usuário o valor do raio e calcule a área do círculo: A = PI * r elevado a 2

constante_pi = 3.14

raio_circulo = int(input("Qual o raio do circulo?"))

area_circulo = constante_pi * raio_circulo ** 2

print(f"Resultado: {area_circulo}")