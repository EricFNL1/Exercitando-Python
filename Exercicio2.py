num = float(input("Insira um número: \n"))

parirmpar = num % 2

if num > 0 and parirmpar == 0:
    print("O número ",num,"é positivo e par")
elif num < 0 and parirmpar != 0:
    print("O número,",num,"É negativo e impar")
if num < 0 and parirmpar == 0:
    print("O número",num, "é negativo e par")
elif num > 0 and parirmpar != 0:
    print("O número", num, "é impar e positivo")

   