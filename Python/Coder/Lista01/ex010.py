"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre 
   em graus Fahrenheit. (27 °C × 9/5) + 32 = 80,6 °F """
   
celsius = int(input("Temperatura em Grau Celsius: "))
fah = (celsius * (9/5)) + 32
print ("A temperatura de {}°C é de {:.0f}°F".format(celsius, fah))
