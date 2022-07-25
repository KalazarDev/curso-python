"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: <br>
            salário bruto. <br>
            quanto pagou ao INSS. <br>
            quanto pagou ao sindicato. <br>
            o salário líquido. <br>
            calcule os descontos e o salário líquido, conforme a tabela abaixo: <br>
           + Salário Bruto : R$ <br>
        -  IR (11%) : R$ <br>
        - INSS (8%) : R$ <br>
        - Sindicato ( 5%) : R$ <br>
        = Salário Liquido : R$ <br>
        Obs.: Salário Bruto - Descontos = Salário Líquido. <br>
"""

valor_hora = float(input('Digite o valor hora que você ganha R$: '))
horas_trabalhadas = int(input('Digite quantas horas você trabalha por mês: '))
salario_bruto = valor_hora * horas_trabalhadas
inss = salario_bruto * 8/100
valor_sindicato = salario_bruto * 5/100
imposto = salario_bruto * 11/100

print(f'Salario bruto R$ {salario_bruto:.2f}')
print(f'IR: R$ {imposto:.2f}')
print(f'Valor de INSS R$: {inss:.2f}')
print(f'Valor Sindicato R$: {valor_sindicato:.2f}')
print(f'Salario Liquido: R$ {salario_bruto - imposto - inss - valor_sindicato}')