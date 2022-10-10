#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num=float(input("Digite um numero: "))

dobro = num*2
triplo = num*3
raiz = num**(1/2)

print("O dobro é {:.2f}. \no Triplo é {:.2f}. \nA Raiz Quadrada é {:.2f}".format(dobro, triplo , raiz))