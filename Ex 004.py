#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela

var1=input("Digite algo:")
print("O tipo primitivo desse valor é: ", type(var1))

print("So tem espaços? ", var1.isspace())
print("É um número? ", var1.isnumeric())
print("É uma letra? ", var1.isalpha())
print("É alfanumérico? ", var1.isalnum())
print("Esta em caixa alta? ", var1.isupper())
print("Esta em minusculas? ", var1.islower())
print("Esta capitatalizada? ", var1.istitle())