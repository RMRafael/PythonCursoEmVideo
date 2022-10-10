#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere U$ 1 = R$ 3,27

real = float(input("Digite o valor que tem na carteira: "))
dolar = real / 3.27

print("Você pode comprar {:.2f} Doláres.".format(dolar))