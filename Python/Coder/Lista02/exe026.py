"""Um posto está vendendo combustíveis com a 
seguinte tabela de descontos:
a - Álcool:
b - até 20 litros, desconto de 3% por litro
c - acima de 20 litros, desconto de 5% por litro
d - Gasolina:
e - até 20 litros, desconto de 4% por litro
f - acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 6,49 o 
preço do litro do álcool é R$ 5,49."""

Com = input("Informe o típo de combustível A-álcool, G-gasolina: ")

if Com == "A":

    QA = int(input('Informe a quantidade de Alcool em litros a ser comprada: '))
    if QA <= 20:
        A = "Álcool"
        bruto = QA * 5.49
        desconto = (bruto*0.03)
        liquido = bruto - desconto
        print("Você escolher abastercer com {}, com a quantidade de {} litros, com desconto de 3% que da {:.2F}R, você ira pagar {:.2f}R$ no final".format(A, QA, liquido))
    elif QA > 20:
        A = "Álcool"
        bruto = QA * 5.49
        desconto = (bruto*0.05)
        liquido = bruto - desconto
        print("Você escolheu abastercer com {}, com a quantidade de {} litros, com desconto de 3% que da {:.2F}R, você ira pagar {:.2f}R$ no final".format(A, QA, liquido))

elif Com == "G":

    QG = int(input('Informe a quantidade de Gasolina em litros a ser comprada: '))
    if QG <= 20:
        G = "Gasolina"
        bruto = QG * 6.49
        desconto = (bruto*0.04)
        liquido = bruto - desconto
        print("Você escolheu abastercer com {}, com a quantidade de {} litros, com desconto de 4% que da {:.2F}R$, você ira pagar {:.2f}R$ no final".format(
            G, QG, desconto, liquido))
    elif QG > 20:
        G = "Gasolina"
        bruto = QG * 6.49
        desconto = (bruto*0.06)
        liquido = bruto - desconto
        print("Você escolheu abastercer com {}, a quantidade de {} litros, com desconto de 6% que da {:.2F}R$, você ira pagar {:.2f}R$ no final".format(
            G, QG, desconto, liquido))
else:
    print("Opçaõ Invalida!")
