# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Digite o preço do 1º produto: ').replace(',','.'))
p2 = float(input('Digite o preço do 2º produto: ').replace(',','.'))
p3 = float(input('Digite o preço do 3º produto: ').replace(',','.'))

if p1 < p2 < p3:
    print(f'O Preço mais barato é o do 1º produto R$ {p1}')
elif p2 < p3:
    print(f'O Preço mais barato é o do 2º Produto R$ {p2}')
elif p3 < p2 < p1:
    print(f'O Preço mais barato é o do 3º Produto R$ {p3}')
else:
    print(f'Todos preços são iguais 1º R$ {p1} 2º R$ {p2} 3º R$ {p3} ')