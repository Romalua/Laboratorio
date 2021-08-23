"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule
   seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""

altura = float(input("Quanto é a sua altura: "))
formula = (72.7*altura) - 58
print("Seu peso ideal com base na sua altura de {:.2f}m é de {:.2f}Kg".format(
    altura, formula))
