"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

"""
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do catero adjacente: "))
# Elevando os valores ao quadrado, somando, e o resultado, elevado a meio (1/2). Elevar a meio é o mesmo que calcular raiz quadrada.
hi = (co **2 + ca **2) ** (1/2) # A soma dos quadrados dos catetos é igual a hipotenusa.
print(f"A hipotenusa vai medir {hi:.2f}.")

# Resolução com importação
import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do catero adjacente: "))
hi = math.hypot(co, ca)

print(f"A hipotenusa vai medir {hi:.2f}.")



