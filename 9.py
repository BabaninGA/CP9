def hl():
	if X%2==1:
		b="нижнее"
	else:
		b="верхнее"
	return b

def cb():
	if X<=36:
		c="купе"
	else:
		c="боковое"
	return c

try:
	print("Введите номер места в плацкартном вагоне")
	X=int(input())
except ValueError:
	print("Номер места может быть только целым числом")
	exit()
if 1<=X<=54:
	print("место:"+hl()+"_"+cb())
elif X>=55:
	print("Нет такого места в плацкартном вагоне")
else:
	print("Номер места не может быть отрицательным числом или нулём")