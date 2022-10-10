# O mesmo professor do desafio anterior quer sorte a aordem de apresentação de trabalhos dos alunos.
# Façam um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle


al1 = str(input("Informe o nome do aluno: "))
al2 = str(input("Informe o nome do aluno: "))
al3 = str(input("Informe o nome do aluno: "))
al4 = str(input("Informe o nome do aluno: "))

lista = [al1, al2, al3, al4]
shuffle(lista)

print("A ordem sera:")
print(lista)

