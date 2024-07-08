#Erros
    #Excelentes para testes
    #Nao realiza o 'stop' no programa
    #Mensagens customizadas quando encontra um erro

'''try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError:
    print("Index nao existe")'''

#Try e except com input
'''valor = 0

while valor != int:
    try:
        valor = int(input("Digite o valor do seu produto: "))
        print(valor)
        break
    except ValueError:
        print("Favor digitar um valor em numeros")


print("Maiis codigo abaixo")'''



# Else e finally

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Favor digitar um valor em numeros")
finally:
    print("Codigo ok")
'''else:
    print("Usuario digitou um valor correto")
    resultado = valor * 2
    print(resultado)'''



print("Maiis codigo abaixo")