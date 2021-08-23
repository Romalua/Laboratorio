"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
   seu peso ideal, utilizando as seguintes fórmulas:
   Para homens: (72.7*h) - 58
   Para mulheres: (62.1*h) - 44.7"""
   
sexo = str(input("Qual é o seu sexo: M-Masculino / F-Feminino:  "))
altura = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7 * altura) - 58 if sexo == "M" else (62.1 * altura) - 44.7

if peso < peso_ideal:
    print('A baixo do peso ideal!')
elif peso == peso_ideal:
    print('Dentro do peso ideal!')
else:
    print('Acima do peso ideal!')
print('Peso: {:.0f} Peso ideal: {:.0f}'.format(peso, peso_ideal))
   