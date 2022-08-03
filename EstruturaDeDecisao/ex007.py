# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
lista = list()

for i in range(0,3):
    n1 = int(input('Digite um numero: '))
    lista.append(n1)

print(f'O Menor numero é {min(lista)} e o maior é {max(lista)}')
    

