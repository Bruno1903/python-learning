# Functions - funcoes
'''
def boas_vindas(nome, quantidade):
    print(f"Ola {nome}")
    print(f"Temos {str(quantidade)} laptops em estoque")

boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 4)
boas_vindas('Linda', 2)
'''
'''
def boas_vindas_Marcos():#Declarando uma funcao
    print("Ola Marcos!")
    print("Temos 5 laptops em estoque")

def boas_vindas_Ronaldo():#Declarando uma funcao
    print("Ola Ronaldo!")
    print("Temos 4 laptops em estoque")

def boas_vindas_Linda():#Declarando uma funcao
    print("Ola Linda!")
    print("Temos 2 laptops em estoque")

boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_Linda()
'''
'''
#Criando uma funcao de soma
def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

def somar_dois_numeros1():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)


somar_dois_numeros()
somar_dois_numeros1()
print(resultado)
'''
'''
##### Argumentos default e non default #####

def boas_vindas(nome, quantidade=6): #A ordem sempre sera, non default e depois default
    print(f"Ola {nome}")
    print(f"Temos {str(quantidade)} laptops em estoque")

boas_vindas('Marcos')
'''
'''
#### Print ou return em funcoes ####
def cliente1(nome):
    print(f"Ola {nome}")

def cliente2(nome):
    return f'Ola {nome}'

x = cliente1("Maria")
y = cliente2("Jose")

print(x)
print(y)
'''

'''
#Funcao com varios argumentos, somando esse argumentos com FOR

def soma(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado

x = soma(2,3,4,7)
print(x)
'''
'''
#Xargs
#Criar uma funcao que armazena numeros e strings (dados)
def agencia(**carro):
    return carro

print(agencia(marca='Gol', cor='Branca', motor=1.0))
print(agencia(marca='Gol', cor='azul', motor=1.0))
print(agencia(marca='Gol', cor='preto', motor=1.0))
'''

'''
#Qual e o numero fatorial de 4
# 4 * 3 * 2 * 1
import math

print(math.factorial(55))
fatorial = 4 * 3 * 2 * 1
print(fatorial)

print(math.ceil(2.7))
'''