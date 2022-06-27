n = int(input("Insira um número: "))
soma = 0
a = n % 10
b = n // 10
while n != 0:
	if a >= 0:
		a = n % 10
		n = n // 10
		soma = soma + a	
print(soma)