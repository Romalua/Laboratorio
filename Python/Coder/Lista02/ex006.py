"""Faça um Programa que leia três números e mostre o maior deles."""
number1 = int(input("Digite o Primeiro Valor: "))
number2 = int(input("Digite o Segundo Valor:"))
number3 = int(input("Digite o Terceiro Valor: "))

if (number1 > number2) and (number1 >number3) :
    print("Numero maior é {}".format(number1))
elif (number2 > number1) and (number2 > number3) :
    print ("Numero maior é {}".format(number2))
else:
    print ("Numero maior é {}".format(number3))