def somar ():
    x = int(input("Digite um numero: "))
    soma = 0
    for i in range(0, x+1):
        soma = soma + i 
    return soma 
    
x = somar()   
print("A soma foi ", x)  