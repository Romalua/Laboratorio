idade = int(input("Insira a sua idade:"))

if(idade >= 5 and idade <= 7):
    print("Sua categoria é infantil A")
elif(idade >= 8 and idade <= 10):
    print("Sua categoria é infantil B")
elif(idade >= 11 and idade <= 13):
    print("Sua categoria é juventil A")
elif(idade >= 14 and idade <= 17):
    print("Sua categoria é juventil B")
elif(idade >= 18):
    print("Sua categoria é Adulto")
else:
    print("idade não permitida")
