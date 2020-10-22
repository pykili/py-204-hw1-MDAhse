a = input ('Введите последовательность цифр ')
b = 0
for i in a:
	if int(i)>b:
		b=int(i)
print('Самое большое из них - ',b)
