# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ').upper().strip()[0]
if letra in 'AEIOU':
    print(f'Você digitou uma vogal: {letra}')
else:
    print(f'Você digitou uma consoante: {letra}')