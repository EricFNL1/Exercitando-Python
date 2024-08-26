num1 = int(input("Insira o primeiro valor: \n "))
num2 = int(input("Insira o segundo valor: \n "))
num3 = int(input("Insira o terceiro valor: \n "))


if num1 > num2 > num3:
    print(num1,num2,num3)
elif num2 > num3 > num1:
    print(num2,num3,num1)
if num3 > num2 > num1:
    print(num3,num2,num1)
elif num1 > num3> num2:
    print(num1,num2,num3)
if num2 > num1 > num3:
    print(num2,num1,num3)
elif num3 > num1 > num2:
    print(num3,num1,num2)