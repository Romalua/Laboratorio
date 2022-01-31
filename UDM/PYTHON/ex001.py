import math  
import random 

def exibirMenu( ):
    print("Menu de Opções")
    print("1. Exibir a raiz quadrada de 9")
    print("2. Exibir a potência de dois numeros")
    print("3. Sortear um nuemero aleatório entre 2 numeros")
    opcao = int(input("OPÇÃO: "))
    if (opcao == 1):
        raiz = math.sqrt(9)
        print("A raiz quadrada de 9 é", raiz)  
    elif(opcao == 2):
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor "))
        pot = math.pow(n1, n2)
        print("A potencia é ", pot)
    elif(opcao ==3 ):
        min = int(input("Informe o menor valor: "))
        max = int(input("Informe o maior valor: "))
        ale = random.randint(min, max)
        print("Sorteou: ", ale)
    else:
        print("Oção informação é invalida!")
        
exibirMenu()        
             