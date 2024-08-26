nome = str(input("Insira seu nome: "))

num1 = int(input("Insira sua primeira nota: \n"))
num2 = int(input("Insira sua segunda nota: \n"))
num3 = int(input("Insira sua terceira nota: \n"))
num4 = int(input("Insira sua quarta nota: \n"))

media = (num1 + num2 + num3 + num4)/4

if media >= 6:
    print(nome,"Sua média  é ", media, "e você foi aprovado")
else:
    print(nome,"Sua média  é ", media, "e você foi reprovado")