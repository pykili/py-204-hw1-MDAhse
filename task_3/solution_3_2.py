a = ''
n = 0
while n < 10:
	a = a + input()
	n = n + 1
b = a[0]
for i in a:
	if i not in b:
		b = b+i
print('алфавит: ',b)
