"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 
R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo 
para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente."""

from time import sleep

print("""--- Lista de Frutas disponiveis ---
                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg""")

morango = input("Vai querer morango? Sim ou Não:")

if morango == "Sim" or "sim" or "s":
   kg = input("Qual a quantidade em Kg: ") 

   media = 
   preco = kg * 2.50   
   if kg > 8 or 