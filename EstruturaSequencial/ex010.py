# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temp_c = float(input('Digite a temperatura em Graus Celsius: ').replace(',', '.'))
temp_f = ((temp_c * 9) / 5) + 32
print(f'A Temperatura em Fahrenheit é de {temp_f} °F') 