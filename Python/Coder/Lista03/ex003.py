"""Faça um programa que leia e valide as seguintes informações:
a Nome: maior que 3 caracteres;
b Idade: entre 0 e 150;
c Salário: maior que zero;
d Sexo: 'f' ou 'm';
e Estado Civil: 's', 'c', 'v', 'd';"""

nome = str(input("informe um nome--> "))
while (len(nome) <= 3):
    nome = str(input("informe um nome--> "))
    
idade =int(input(input("Idade: ")))
while ( idade > 150 or idade < 0 ):
    idade=int(input("informe a idade--> "))
