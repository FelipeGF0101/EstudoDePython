"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendop que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

"""
km = float(input("Quantos quilômetros foram percorrido? " ))

dia = int(input("Por quantos dias o veículo permaneceu em seu poder? "))

calc = (dia * 60) + (km * 0.15) # Os parêntese não são necessários aqui, porém dão um aspecto mais organizado.

print(f"O valor total a ser pago será de R$ {calc} reais.")

print("=================================================================")
# UMA FORMA UM POUCO MAIS DETALHADA

km1 = float(input("Quantos quilômetros foram percorridos? "))

dia1 = int(input("Por quantos dias o veículo permaneceu em seu poder? "))
print("=================================================================")
calc1 = dia1 * 60

print(f"Valor total das DIÁRIAS é de: R$ {calc1}")
print("=================================================================")
calc2 = km1 * 0.15

print(f"Valor total por QUILÔMETROS RODADOS é de: R$ {calc2}")
print("=================================================================")
calc3 = calc1 + calc2

print(f"O valor TOTAL a pagar será de: R$ {calc3}")
print("=================================================================")
desc = calc3 - (10/100*calc3)
print(f"Caso o pagamento seja feito em dinheiro, o valor final terá um abatimento de 10%. Sendo assim, o valor a ser pago será de R$ {desc} reais.")
print("=================================================================")
