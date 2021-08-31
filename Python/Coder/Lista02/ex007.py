"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

from time import sleep
num1 = int(input("Digite o Primeiro Valor: "))
num2 = int(input("Digite o Segundo Valor: "))
num3 = int(input("Digite o Terceiro Valor: "))

maior = num1
menor = num1
if num2 > maior and num2 > num3:
    maior = num2
if num3 > maior and num3 > num2:
    maior = num3
if num2 < menor and num3 < num2:
    menor = num2
if num3 < menor and num3 < num2:
    menor = num3

print('\n')
print('-=-' * 20)
print('Processando...')
sleep(1)
print('\nO valor mais alto é {}\nO valor mais baixo é {}\n'.format(maior, menor))
print('-=-' * 20)
print('\n')
