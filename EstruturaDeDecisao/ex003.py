# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -    Feminino, M - Masculino, Sexo Inválido.
sexo = input('Digite o seu Sexo: ').upper().strip()[0]

if sexo == 'F':
    print('Você digitou sexo Feminino')
elif sexo == 'M':
    print('Você digitou Sexo Masculino')
else:
    print('Sexo Invalido')
