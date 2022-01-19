"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar. O resultado da operação deve ser
acompanhado de uma frase que diga se o número é:
A -par ou ímpar;
B -positivo ou negativo;
C -inteiro ou decimal."""

numero = float(input('Digite um inteiro: '))

if numero%2 :
        print("A-Ímpar")
else:
        print("A-Par")
        
if numero >= 0 : 
        print ("positivo")
else:
        print ("Negativo")
        
        
if(numero // 1 == numero): 
    print('Número inteiro !')
else:
    print('Número Decimal !')        
        