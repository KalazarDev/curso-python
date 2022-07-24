# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. <br>
# C = 5 * ((F-32) / 9).

temp_f = float(input('Digite a temperatura em Fahrenheit para converter: ').replace(',','.'))
temp_c = 5 * ((temp_f - 32) / 9)
print(f'A Temperatura em graus Celsius é de {temp_c:.2f} °C')