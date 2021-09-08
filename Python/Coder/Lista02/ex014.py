"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à 
tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

from time import sleep
nt1 = float(input("Primeira nota: "))
nt2 = float(input("Segunda nota: "))
media = (nt1 + nt2)/2

if media >= 9.0 and media <= 10.0 :
    conceito = "A"
    status = 'Aprovado'
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSuas Notas: {} e {}".format(nt1,nt2))
    print("\nMédia das Notas: {}".format(media))
    print("\nConceito: {}".format(conceito))
    print("\nStatus:{}".format(status))
    print('-=-' * 20)
    print('\n')
    
elif media >= 7.5 and media <= 9.0 :
    conceito = "B"
    status = 'Aprovado'
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSuas Notas: {} e {}".format(nt1,nt2))
    print("\nMédia das Notas: {}".format(media))
    print("\nConceito: {}".format(conceito))
    print("\nStatus:{}".format(status))
    print('-=-' * 20)
    print('\n')
    
elif media >= 6.0 and media <= 7.5 :
    conceito = "C"
    status = 'Aprovado'
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSuas Notas: {} e {}".format(nt1,nt2))
    print("\nMédia das Notas: {}".format(media))
    print("\nConceito: {}".format(conceito))
    print("\nStatus:{}".format(status))
    print('-=-' * 20)
    print('\n')
    
elif media >= 4.0 and media <= 6.0 :
    conceito = "D"
    status = 'Reprovado'
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSuas Notas: {} e {}".format(nt1,nt2))
    print("\nMédia das Notas: {}".format(media))
    print("\nConceito: {}".format(conceito))
    print("\nStatus:{}".format(status))
    print('-=-' * 20)
    print('\n')   
    
elif media < 4.0:
    conceito = "E"
    status = 'Reprovado'
    print("\n")
    print("-=-" * 20)
    print("Processando...")
    sleep(1)
    print("\nSuas Notas: {} e {}".format(nt1,nt2))
    print("\nMédia das Notas: {}".format(media))
    print("\nConceito: {}".format(conceito))
    print("\nStatus: {}".format(status))
    print('-=-' * 20)
    print('\n')        
