# Lambda Function
    #É uma funcao (pequena) sem nome
    #Pode ter varios argumentos mas somente 1 expressao
    #Muito utilizada dentro de outras funcoes
    #Codigo mais "Clean"

"""def somar(x):
    return x + 10

print(somar(2))"""

"""somar = lambda x,y: x + y + 10

print(somar(10,11))"""

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))