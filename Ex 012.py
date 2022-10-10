#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: "))

npreco = preco*0.95

print("O valor com desconto é: R$ {:.2f}.".format(npreco))
