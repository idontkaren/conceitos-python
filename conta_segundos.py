seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))
a = seg // 86400 
seg_res = seg % 86400 
b = seg_res // 3600
seg_res1 = seg_res % 3600
c = seg_res1 // 60
d = seg_res1 % 60
print(a," dias, ",b," horas, ",c," minutos e ",d," segundos.")