#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

soma = 0

for n in range(1, 5):
    nota = float(input(f'Digite a {n}º Nota: '))
    soma += nota

print(f'A media do Aluno foi {soma/4}')