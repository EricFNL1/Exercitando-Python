num = int(input("Insira um valor para receber a tabuada: "))

max = num * 11

print("Tabuada do número: ",num)

for i in range(num,max, num):
    print(i)