# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n1 = int(input('Digite um numero, pode ser negativo: '))
if n1 < 0:
    print(f'O Numero {n1} é negativo')
else:
    print(f'O Numero {n1} é Positivo')