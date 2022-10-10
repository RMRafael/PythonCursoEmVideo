#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias=int(input("Informe a quantidade de dias que o carro foi alugado: "))
km = float(input("Informe a quantidade de KM percorrida: "))
preco = dias*60 + 0.15*km

print("Você rodou {} km durante {} dias, o valor do aluguel é R$ {:.2f}.".format(km, dias, preco))