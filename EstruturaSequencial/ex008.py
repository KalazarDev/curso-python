# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('Qual o valor hora do seu salario: R$ ').replace(',', '.'))
horas_trabalhadas = int(input('Quantas horas você trabalha por mês? '))
print(f'O valor do seu salario no mês é de R$ {salario_hora * horas_trabalhadas:.2f}')
