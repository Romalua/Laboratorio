"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo = str(input("Qual é o seu sexo: M-Masculino / F-Feminino:  "))

if sexo == "M":
    print("Sexo é Masculino")
else:
    print("Sexo é Feminino")
