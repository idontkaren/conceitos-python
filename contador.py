seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))
a = seg // 86400
b = seg % 3600
c = b / 60
d = b % 60
print(a, "dias, ",b," horas, ",c, " minutos e ",d, "segundos.") 