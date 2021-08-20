"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta
   área para o usuário."""

lado = float(input("Lado do Quadrado: "))
soma = lado * lado 
dobro = soma * 2
print ("A valor da área do quadrado é {:.0f} e o dobro dessa área é {:.0f}".format(soma,dobro))
