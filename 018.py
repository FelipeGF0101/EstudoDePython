"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""
import math

ang = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ang)) # O valor precisa ser convertido para radianos.
print(f"O ângulo de {ang} tem o SENO de {seno:.3f}.")

cosseno = math.cos(math.radians(ang))
print(f"O ângulo de {ang} tem o COSSENO de {cosseno:.3f}.")

tangente = math.tan(math.radians(ang))
print(f"O ângulo de {ang} tem a TANGENTE de {tangente:.3f}.")


# OUTRA FORMA DE FAZER:

# Na fase da importação da biblioteca, basta definir quais funcionalidades iremos usar. Assim não há necessidade de usar a referência 'math' antes das funcionalidades.

# from math import radians, sin, cos, tan

# ang = float(input("Digite o ângulo que você deseja: "))
# seno = sin(radians(ang)) # O valor precisa ser convertido para radianos.
# print(f"O ângulo de {ang} tem o SENO de {seno:.3f}.")

# cosseno = cos(radians(ang))
# print(f"O ângulo de {ang} tem o COSSENO de {cosseno:.3f}.")

# tangente = tan(radians(ang))
# print(f"O ângulo de {ang} tem a TANGENTE de {tangente:.3f}.")

