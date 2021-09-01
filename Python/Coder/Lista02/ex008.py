"""Faça um programa que pergunte o preço de três produtos e informe qual produto você 
   deve comprar, sabendo que a decisão é sempre pelo mais barato."""

from time import sleep
produto1 = float(input("Preço do primeiro produto: "))
produto2 = float(input("Preço do segundo produto: "))
produto3 = float(input("Preço do terceiro produto: "))

barato = produto1
if produto2 < barato and produto2 < produto3:
    barato = produto2
if produto3 < barato and produto3 < produto2:  
    barato = produto3  

print("\n")    
print("-=-" *20)
print("Processando...")
sleep(1) 
print("\nO menor preço é do produto {}".format(barato))
print('-=-' * 20)
print('\n')

     
    
   