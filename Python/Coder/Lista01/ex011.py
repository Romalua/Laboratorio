""" 
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo"""

number1 = int(input("1° Numero é Inteiro: "))
number2 = int(input("2° Numero é Inteiro: "))
number3 = float(input("3° Numero é Real: "))

soluc1 = (number1*2) + (number2/2)
soluc2 = (number1*3) + number3
soluc3 = (number3 ** 3)

print("O produto do dobro de {:.0F} com metade de {:.0F} é {:.0F}".format(
    number1, number2, soluc1))
print("A soma do triplo de {:.0F} com o valor de {:.0F} é {:.0F}".format(
    number1, number3, soluc2))
print("O valor de {:.0F} elevado ao cubo é {:.0F}".format(number3, soluc3))
