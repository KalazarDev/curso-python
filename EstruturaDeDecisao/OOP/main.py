
from datetime import datetime
# POO
# Classes
# 1.1 Utilizadas para criar Objetos
# 1.2 Objetos são partes dentro de uma Class
# 1.3 Classes são utilizadas para agrupar dados e funções podendo reutilizar

# Class: Frutas
# Objects: Abacate, Banana

# Criar a Classe
class Funcionarios:

    def __init__(self,nome,sobrenome,ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        
        
    


# Criar o Objeto
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol','Silva', 2005)
# print(usuario1.nome_completo())

print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))

# # criar os parametros do usuario1
# usuario1.nome = 'Elena'
# usuario1.sobrenome = 'Cabral'
# usuario1.data_nascimento = '12/01/2009'

# # criar os parametros do usuario2
# usuario2.nome = 'Carol'
# usuario2.sobrenome = 'Silva'
# usuario2.data_nascimento = '15/10/2005'

# print
print(usuario1.nome, usuario1.sobrenome)
print(usuario2.nome, usuario2.sobrenome)

