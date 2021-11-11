combustivel = str(input("Digite o tipo de combustível que você colocou:")). strip().capitalize() #pede a pessoa que coloque o tipo de combustível.

litro = float(input ("Digite a quantidade de litros que você colocou:")) #pede a pessoa que coloque a quantidade de litros.

if combustivel == "A": #se o tipo do combustível escolhido for igual a Álcool execute isto:

alcool = 3.5 #define o preço do álcool.

custo = litro * alcool #cria a variável custo que recebe a variável litro com a quantidade de litros que o usuário colocou e multiplica pelo preço do litro do álcool.

if litro <= 20: #se a quantidade de litros for menor ou igual a 20 execute isto:

desconto1 = (custo * 3)/100 #define que a variável desconto1 vai receber a multiplicação do desconto da primeira condição vezes o custo do litro,divido por 100

print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto1,custo-desconto1)) #escreve na tela o valor do desconto e o valor atual do combustível

elif litro > 20: #se o valor do litro for maior que 20 execute isto:

desconto2 = (custo * 5)/100 #define o desconto se a quantidade de litros colocados for maior que 20

print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto2,custo-desconto2)) #escreve na tela o valor do desconto e o preço atual a pagar

