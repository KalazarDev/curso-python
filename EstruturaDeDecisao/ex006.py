# 6. Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 > n3:
    print(f'O numero {n1} é o maior')
elif n2 > n3:
    print(f'O numero {n2} é o maior')
else:
    print(f'O numero {n3} é o maior')