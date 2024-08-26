A = int(input("Informe o valor do Lado A: "))
B = int(input("Informe o valor do Lado B: "))
C = int(input("Informe o valor do Lado C: "))


if A == B == C:
    print("Equilátero")
elif A != B != C:
    print("Escaleno")
else:
    print("isóceles")