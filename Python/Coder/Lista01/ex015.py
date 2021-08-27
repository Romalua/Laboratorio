"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um 
programa que nos dê:

A salário bruto.
B quanto pagou ao INSS.
C quanto pagou ao sindicato.
D o salário líquido.
E calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

money_hora = int(input("Valor recebido por hora: "))
mes_hora = int(input("Número de horas trabalhadas no mês: "))
#print ("Total do seu salário do mês: {}".format(money_hora*mes_hora))
bruto = (money_hora*mes_hora)
imposto_renda = bruto * 0.11
inss = bruto * 0.08
sindi = bruto * 0.05
liquido = bruto - (imposto_renda + inss + sindi)

print("+ Salário Bruto: {}R$ \n - IR (11%) : {}R$ \n - INSS (8%) : {}R$ \n - Sindicato (5%) : {}R$ \n Sálario Liquido : {}R$ ".format(bruto,
                                                                                                                                      imposto_renda, inss, sindi, liquido))
