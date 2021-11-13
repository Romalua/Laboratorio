import math
print("========== Menu Principal ==========",
      "\n1. Calcular a potência X elevado a Y",
      "\n2. Calcular a raiz quadrada de um número",
      "\n3. Verificar se um número é par ou ímpar",
      "\n=================================")
escolha = int(input("Escolha a opção por favor: "))

if escolha == 1:
    x = float(input("Insira o valor de X: "))
    y = float(input("Insira o valor de Y: "))
    potenciacao = (x**y)
    print("Potência de {:.0f} elevado a {:.0f} é {:.0f} ".format(
        x, y, potenciacao))
elif escolha == 2:
    number = float(input("Digite o número para o calculo de raiz quadrada:"))
    raiz = math.sqrt(number)
    print("\nA raiz quadrada de {:.0f} é {:.2f}".format(number, raiz))
elif escolha == 3:
    valor = int(input("Digite o numero: "))
    if (valor % 2) == 0:
        print("Numero digitado é Par")
    else:
        print("Numero digitado é Impar")
else:
    print("opção digitada é inválida!!!")
]