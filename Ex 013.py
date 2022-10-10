#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sal = float(input("Digite o salário do funcionário: "))

nsal = sal*1.15

print("O novo salário sera de R$ {:.2f}".format(nsal))