"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

"""
print('Digite a quantidade metros que deseja converter: ')
met=float(input())

cent=met*100
mili=met*1000 

print(f'{met} metros equivale a {cent} centímetros e {mili} milímetros.')
