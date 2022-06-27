n = int(input("Digite a quantidade de impares que deseja: "))
a = 0
n = n - 1
while a <= n * 2:
	a += 1	
	if a % 2 != 0:
		print(a)