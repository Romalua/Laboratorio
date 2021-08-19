nome = "Lucas Andre"
idade = 32 # int 
altura = 1.80 #float 
e_maior = idade > 18 #bool
peso = 65
imc = peso / (altura **2)

print ("Nome: {} tem {} anos, seu imc é {:.1f}".format (nome, idade, imc))
print ("Nome: {n} tem {i} anos, seu imc é {im:.2f}".format (n=nome, i=idade, im=imc))