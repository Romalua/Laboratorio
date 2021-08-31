"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

alfa = input("Digite um letra: ")

if alfa.isalpha():
    if alfa == "a":
        print("Vogal")
    elif alfa == "e":
        print("Vogal")
    elif alfa == "i":
        print("Vogal")
    elif alfa == "o":
        print("Vogal")
    elif alfa == "u":
        print("Vogal")
        print("Insira uma letra ou consoante")
    else:
        print("Consoante")
else:
    print("Não é uma letra!")
