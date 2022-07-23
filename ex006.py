# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi

r = int(input('Digite o raio do circulo: '))
a = pi * pow(r, 2)
print(f'A area do circulo é {a:.0f} m²')
