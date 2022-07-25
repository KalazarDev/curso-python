"""
 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
"""
tamanho = float(input('Digite o tamanho do arquivo em MB: '))
internet = int(input('Digite a velocidade de sua internet: '))
download_link = internet / 8
velocidade = tamanho / download_link

print(f'Seu link de {internet} MB e a velocidade de transmissão é de {download_link} MB e você vai levar {velocidade/60:.2f} minutos para baixar o arquivo') 
