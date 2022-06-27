import math
num = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))
num3 = int(input("Insira um número: "))
num4 = int(input("Insira um número: "))

x1 = num
y1 = num2
x2 = num3
y2 = num4

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if d >= 10:
	print("longe")
else:
	print("perto")


