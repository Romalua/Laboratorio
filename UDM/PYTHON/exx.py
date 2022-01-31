"""Faça um programa que leia 5 números e informe a média 
dos números ímpares digitados. Utilize o laço de repetição 
for."""

        
s = 0
con = 0
for c in range(1, 6):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 1 < 0:
        s += n
        con += 0
print('{} números são pares e a soma deles é: {}'.format(con, s))
