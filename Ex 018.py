#Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import radians, sin, tan, cos
#radians converte o angulo em Graus para Radianos

ang = float(input("Qual o valor do angulo? "))

print("Seno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}".format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))