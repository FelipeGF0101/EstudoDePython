"""
Escreva um programa que converta uma temperatura digitada em ºC para ºF.
"""
temp = float(input("Digite a temperatura em ºC: "))

f = temp * 1.8 + 32

print(f"{temp} ºC (graus celsius) equivale a {f} ºF (graus Fahrenheit).")

print("====================================================")
# Convertendo Fahrenheit para Celsius

temp1 = float(input("Digite a temperatura em ºF: "))

c = (temp1 - 32)/1.8

print(f"{temp1} ºF (graus fahrenheit) equivale a {c} ºC (graus celsius).")