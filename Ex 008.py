#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input("Digite uma medida metros: "))
cm = m * 100
mm = m * 1000
dc = m / 10
hc = m / 100
km = m / 1000
print("A medida inserida equivale a:\n {:.0f} cm\n {:.0f} mm\n {:.2f} dc \n {:.2f} hc \n {:.2f} km".format(cm, mm, dc, hc, km))