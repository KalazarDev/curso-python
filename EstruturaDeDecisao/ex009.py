# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
lista = [n1, n2, n3]

print(f'Os numeros digitados em ordem descrente: {sorted(lista, reverse=True)}')
