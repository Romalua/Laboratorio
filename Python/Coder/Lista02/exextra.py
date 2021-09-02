"""Crie um algoritmo que leia a quantidade de gibis e revistas vendidas em uma banca
em um dia. 
Sabe-se que os Gibis custam R$ 3,50, enquanto revistas custam o dobro. 
A comissão da venda dos gibis é de 3%, já a de revista é de 5%, calculados com base
no valor total arrecadado no dia com a venda de gibis e revistas.
Sabe-se que é repassado ao fornecedor o valor de 50% da venda diária (já sem os
valores das comissões).
Apresente ao usuário:
- O valor total arrecadados com a venda de gibis, com a venda de revistas, e 
com a venda de gibis e revistas juntos.
- O valor da comissão de venda dos gibis e das revistas
- O valor que será repassado ao fornecedor"""

gibis = int(input("Quantidade de gibis vendidas no dia: "))
revista = int(input("Quantidade de revista vendidas no dia: "))

vendas_gibis = (gibis * 3.50)
vendas_revista = (revista * 7.00)
vendas_combinada = (vendas_gibis + vendas_revista)
comissao_gibis = (3.50 * gibis) * 0.03
comissao_revista = (7.00 * revista) * 0.05
fornecedor = (vendas_combinada - (comissao_revista + comissao_gibis)) / 2

print("\nValor total arrecadados com a venda de gibis:  R${:.2f}".format(
    vendas_gibis))
print("\nValor total arrecadados com a venda de revista:  R${:.2f}".format(
    vendas_revista))
print("\nValor total arrecadados com a venda de ambos (revista e gibis):  R${:.2f}".format(
    vendas_combinada))
print("\nValor da comissão de venda dos Gibis R${:.2f} e das Revistas R${:.2f}".format(
    comissao_gibis, comissao_revista))
print("\nValor repassado ao fornecedor:  R${:.2f}".format(fornecedor))
