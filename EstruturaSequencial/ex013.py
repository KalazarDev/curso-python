"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Digite sua altura: ').replace(',', '.'))
sexo = str(input('Digite seu Sexo (M/F): ').upper())

if sexo == 'F':
    print(f'Seu Peso ideal é de: {(62.1 * altura) - 44.7:.2f}')
if sexo == 'M':
    print(f'Seu peso ideal é de: {(72.7 * altura) - 58:.2f}')
    