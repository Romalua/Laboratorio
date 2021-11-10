"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar. O resultado da operação deve ser
acompanhado de uma frase que diga se o número é:
A -par ou ímpar;
B -positivo ou negativo;
C -inteiro ou decimal."""

import math
print("-- Digite  dois números --")
num1 = int(input("Primeiro Valor: "))
num2 = int(input("Segundo Valor: "))
print(
    "========== Menu Principal ==========",
      "\n1. Adição",
      "\n2. Subtração",
      "\n3. Multiplicação",
      "\n4. Divisão",
      "\n=================================")
escolha = int(input("Escolha a opção por favor: "))

if escolha == 1:
    adicao=(num1 + num2) 
    print("Resultado é {}".format(adicao))
    valor = adicao 
    if (valor%2) ==0:
        print("{} é PAR".format(valor))
    else:
        print("{} é IMPAR".format(valor))
        tipo = adicao
    if (valor>0) :
            print("{} é Positivo".format(tipo))
    else:
            print("{} é Negativo".format(tipo))
 
        

elif escolha == 2:
   subtracao=num1 - num2
   print("Resultado é {}".format(subtracao))

elif escolha == 3:
    Multiplicacao=num1 * num2
    print("Resultado é {}".format(Multiplicacao))

elif escolha == 4:
    divisao=num1 / num2
    print("Resultado é {}".format(divisao))

else:
    print("Opção Inválida")
