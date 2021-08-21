"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
temperatura em graus Celsius. C = 5 * ((F-32) / 9)."""

fhar = int(input("Temperatura em graus Fahrenheit: "))
conv = 5 * ((fhar-32)/9)
print("A temperatura convertida é de {:.0f}°C".format(conv))
