#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))
area = larg*alt
tinta = area / 2
print("Sua parede de {} x {} tem {:.2f} m²".format(larg, alt ,area))
print("Você vai precisar de {:.2f} litros para pintar a parede.".format(tinta))