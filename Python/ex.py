import random
num = 20
acertou = 0
errou = 0

while(num > 0):
    
    num = int( input("Digite um numero de 1 a 5: ") )
    
    if (num <= 0):
        print ("Ok, saindo do programa...")
        break
    
    aleatorio = random.randint(1, 5)
    
    if(num== aleatorio):
        print ("Voce acerto o numero", aleatorio)
        acertou = acertou + 1
    else:
        print("Voce erro, o numero sorteado é ", aleatorio)
        errou += 1 

    print("----------------------")
print("------ Relatório -----")
print(f"Você acertou {acertou} vezes.")
print(f"voce errou {errou} vezes.")
print("----------------------")
