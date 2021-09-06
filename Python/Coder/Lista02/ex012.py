"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são
do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de
horas trabalhadas no mês.
Desconto do IR:
-Salário Bruto até 900 (inclusive) - isento
-Salário Bruto até 1500 (inclusive) - desconto de 5%
-Salário Bruto até 2500 (inclusive) - desconto de 10%
-Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.

No exemplo o valor da hora é 5 e a quantidadede hora é 220.3
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

from time import sleep

money_time = float(input("Dinhero por Hora trabalhada: "))
money_day = float(input("Horas Trablhadas: "))
bruto = (money_time * money_day)

if bruto <= 900:
    desc_sindicato = (bruto/100)*3
    fgts = (bruto/100)*11
    ir = 0
    liquido = bruto - desc_sindicato
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSalário Bruto R${:.2f}".format(bruto))
    print("\nDesconto Sindicato {:.2f}".format(desc_sindicato))
    print("\nDesconto IR R${:.2f}".format(ir))
    print("\nFGTS R${:.2f}".format(fgts))
    print("\nSalário Liquido R${:.2f}".format(liquido))
    print('-=-' * 20)
    print('\n')

elif bruto <= 1500:
    desc_sindicato = (bruto/100)*3
    fgts = (bruto/100)*11
    ir = (bruto/100)*5
    liquido = bruto - desc_sindicato - ir
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSalário Bruto R${:.2f}".format(bruto))
    print("\nDesconto Sindicato {:.2f}".format(desc_sindicato))
    print("\nDesconto IR R${:.2f}".format(ir))
    print("\nFGTS R${:.2f}".format(fgts))
    print("\nSalário Liquido R${:.2f}".format(liquido))
    print('-=-' * 20)
    print('\n')

elif bruto <= 2500:
    desc_sindicato = (bruto/100)*3
    fgts = (bruto/100)*11
    ir = (bruto/100)*10
    liquido = bruto - desc_sindicato - ir
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSalário Bruto R${:.2f}".format(bruto))
    print("\nDesconto Sindicato {:.2f}".format(desc_sindicato))
    print("\nDesconto IR R${:.2f}".format(ir))
    print("\nFGTS R${:.2f}".format(fgts))
    print("\nSalário Liquido R${:.2f}".format(liquido))
    print('-=-' * 20)
    print('\n')

else:
    desc_sindicato = (bruto/100)*3
    fgts = (bruto/100)*11
    ir = (bruto/100)*20
    liquido = bruto - desc_sindicato - ir 
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSalário Bruto R${:.2f}".format(bruto))
    print("\nDesconto Sindicato {:.2f}".format(desc_sindicato))
    print("\nDesconto IR R${:.2f}".format(ir))
    print("\nFGTS R${:.2f}".format(fgts))
    print("\nSalário Liquido R${:.2f}".format(liquido))
    print('-=-' * 20)
    print('\n')
