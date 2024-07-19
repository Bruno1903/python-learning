altura = float(input("Qual é a sua altura em cm: "))
peso = float(input("Qual é o seu peso em kg: "))
imc = float(peso / (altura * altura))

if imc < 18.5:
    print("MAGREZA")
elif imc < 25:
    print("NORMAL")
elif imc < 30:
    print("SOBREPESO")
elif imc < 40:
    print("OBESIDADE")
else:
    print("OBESIDADE GRAVE")
