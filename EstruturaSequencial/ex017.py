"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. <br>
        Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: <br>
        comprar apenas latas de 18 litros; <br>
        comprar apenas galões de 3,6 litros; <br>
        misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. <br>
"""


from math import ceil


area = int(input('Digite a area a ser pintada em m²: '))
litros = area / 6
total = int(litros)
latas_18 = 0
latas_3_6 = 0

print(f'Comprar apenas Latas de 18 Litros: {ceil(total / 18)} no valor de R$ {ceil(total / 18) * 80}')
print(f'Comprar apenas Galões de 3,6L: {ceil(total/3.6)} no valor de R$ {ceil(total/3.6) * 25}')
while litros > 0:
    if litros / 18 >= 1:
        latas_18 += 1
        litros -= 18
    if litros / 18 <= 1:
        latas_3_6 += 1
        litros -= 3.6

print(f'Para Misturar você vai precisar de {round((latas_18) + (latas_18 * 10/100))} galões de 18L e {round((latas_3_6) + (latas_3_6 * 10/100))} galões de 3.6L com o custo de R$ R$ {round((latas_18) + (latas_18 * 10/100)) * 80 + round((latas_3_6) + (latas_3_6 * 10/100)) * 25 } ')        





