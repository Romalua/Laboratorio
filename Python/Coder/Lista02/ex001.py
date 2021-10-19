"""Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:

a) o novo peso se a pessoa engordar 15% sobre o peso digitado;

b) o novo peso se a pessoa emagrecer 20% sobre o peso digitado. """

peso = float(input("Digite seu Peso: "))
engordar = (peso * 0.15) + peso
emagrecer = peso - (peso * 0.20)

print("Seu peso ao engordar 15% seria de {:.1f}KG ao emagrecer 20% seria {:.1f}KG".format(
    engordar, emagrecer))
