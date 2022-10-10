#Um professor quer sortear um dos seus quatro alunios para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

al1 = input("Informe o nome do aluno: ")
al2 = input("Informe o nome do aluno: ")
al3 = input("Informe o nome do aluno: ")
al4 = input("Informe o nome do aluno: ")
lista = [al1, al2, al3, al4]
escolhido = choice(lista)

print("{} foi o aluno escolhido.".format(escolhido))