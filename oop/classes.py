#Python Object-Oriented Programming

#Classes
    #Utilizadas para criar objetos (instances)
    #Objetos sao partes dentro de uma class (instancias)
    #Classes sao utilizadas para agrupar dados e funcoes, podendo reutilizar
    #=======
    #Class: Frutas
    #Objects: Abacate, Banana...

'''class Funcionarios:
    nome = "Elena"
    sobrenome = "Cabral"
    data_nascimento = "12/01/2009"

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)'''

#====================================

#Criando objetos dentro de uma classe

#Criar a classe
class Funcionarios:
    pass


#Criando o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()


#Criando os parametros do usuario1
usuario1.nome = "Elena"
usuario1.sobrenome = "Cabral"
usuario1.data_nascimento = "12/01/2009"


#Criando os parametros do usuario2
usuario2.nome = "Carol"
usuario2.sobrenome = "Silva"
usuario2.data_nascimento = "15/10/2005"

#Print
print(usuario2.nome)