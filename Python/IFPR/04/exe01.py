import random
import math

print("<--Menu de Opções-->")
print("1.Somar 2 Números")
print("2.Potência y de um numero x (x elevado a y)")
print("3. Raiz quadrada de x ")
print("4.Gerar um número aleatório")
print("<--Escolha Opção-->")
opcao = int(input("Opção: "))
if (opcao == 1):
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    print("A soma dos valores é ", (numero1+numero2))
elif(opcao == 2):
    x = int(input("Valor de X: "))
    y = int(input("Valor de y: "))
    print("Valor de {} elevado a {} é {}".format(x, y, (x**y)))
elif(opcao == 3):
    numero = int(input("Valor de X: "))
    raiz = math.sqrt(numero)
    print("A raiz quadrade de {} é {:.2f}".format(numero,raiz))
elif(opcao == 4):
    x = random.random()
    print("Numero aletório", x)
