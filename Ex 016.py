#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a asua porção inteira.

import math

num = float(input("Digite um número real:"))
inte = math.floor(num)

print("O numero {} tem a parte inteira {:.0f}.".format(num, inte))