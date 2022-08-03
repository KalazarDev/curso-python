# 1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira outro numero: '))

if n1 > n2:
    print(f'O Numero {n1} é maior que {n2}')
else:
    print(f'O numero {n2} é maior que {n1}')