"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
           o produto do dobro do primeiro com metade do segundo .
           a soma do triplo do primeiro com o terceiro.
           o terceiro elevado ao cubo. 
           
           Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 
           Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
           
           Para homens: (72.7*h) - 58 
           Para mulheres: (62.1*h) - 44.7 
           João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 
"""
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = float(input('Digite um numero Real: '))
print('__' * 30)
print(f'O Produto do Dobro do Primeiro com metade do segundo: {int((n1 * 2) + (n2 / 2))}')
print(f'A soma do triplo do primeiro com o terceiro: {(n1 * 3) + n3}')
print(f'O terceiro elevado ao cubo: {n3 ** 3}')
