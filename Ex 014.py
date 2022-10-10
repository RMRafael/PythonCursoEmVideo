#Escreva um programa que converta uma temperatura digita em ºC e converta para ºF.

celsius = float(input("Digite a temperatura em ºC: "))
far = celsius*1.8 + 32

print("A temperatura de {:.1f} ºC equivale a {:.1f} ºF.".format(celsius, far))