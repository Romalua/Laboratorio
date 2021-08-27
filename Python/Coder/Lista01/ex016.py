"""Faça um programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura
da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
de latas de tinta a serem compradas e o preço total."""

metros_area = float(
    input("Tamanho em metros quadrados da área a ser pintada: "))
litros = metros_area/3
preco = 80.0
lata_tamanho = 18



lata_full = litros / lata_tamanho
total = lata_full * preco

print ("- Você usara {} lata de tinta. \n - O preço total é de: R${}" .format(lata_full, total))


"""metros = input("Digite a quantidade de metros quadrados a serem pintados: ")
litros = metros/3

precoL = 80.0
capacidadeL = 18

latas = litros / capacidadeL
total = latas * precoL

print 'Você usara ',latas,'latas de tinta'
print 'O preco total é de: R$',total
"""
