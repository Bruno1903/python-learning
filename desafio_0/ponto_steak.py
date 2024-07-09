temperatura = int(input("Qual é a temperatura da carne? "))

if temperatura <= 47:
    print("Cozinhar por mais alguns minutos!")
elif temperatura <= 53:
    print("Selada!")
elif temperatura <= 59:
    print("Ao ponto para mal!")
elif temperatura <= 64:
    print("Ao ponto!")
elif temperatura <= 70:
    print("Ao ponto para bem!")
else:
    print("Bem passada")

