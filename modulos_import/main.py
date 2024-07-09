#import funcoes #Assim voce importa todos de uma vez
from funcoes import somar, multi, find_index #Assim voce importa apenas a funcao que precisa
from items.cadastro import cliente

somar()
multi()
cliente()

list1 = ["a", "b", "c", "d", "e"]

var1 = find_index(list1, "y")
print(var1)