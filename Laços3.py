teste = 0
resultado = 0

while teste !=1:
    valor = int(input("Insira um número: "))
    resultado +=valor
    if valor == 0:
        print("A soma é", resultado)
        break