"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte 
    critério, baseado no salário atual:
    -salários até R$ 280,00 (incluindo) : aumento de 20%
    -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    -salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
    informe na tela:
    -o salário antes do reajuste;
    -o percentual de aumento aplicado;
    -o valor do aumento;
    -o novo salário, após o aumento."""


from time import sleep
money = float(input("Seu money mensal: "))

if money <= 280:
    ajuste = (money * 0.20)
    aumento = money + ajuste
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSalário antes do reajuste R${}".format(money))
    print("\nPercentual de aumento aplicado - 20%")
    print("\nValor do aumento R${}".format(ajuste))
    print("\nNovo salário R${}".format(aumento))
    print('-=-' * 20)
    print('\n')
