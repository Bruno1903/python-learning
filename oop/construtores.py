#Constructors
from datetime import datetime
class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


#Criando o objeto
usuario1 = Funcionarios("Elena", "Cabral", 2009)
usuario2 = Funcionarios("Carol", "Silva", 2005)
usuario3 = Funcionarios("Bruno", "Almeida", 2001)


#Print basico
'''print(usuario1.nome)
print(usuario2.nome)
print(usuario3.sobrenome)'''

#print nome e sobrenome usando a funcao nome_completo
print(usuario2.nome_completo())
print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario3))


'''
#Criando os parametros do usuario1
usuario1.nome = "Elena"
usuario1.sobrenome = "Cabral"
usuario1.data_nascimento = "12/01/2009"


#Criando os parametros do usuario2
usuario2.nome = "Carol"
usuario2.sobrenome = "Silva"
usuario2.data_nascimento = "15/10/2005"
'''