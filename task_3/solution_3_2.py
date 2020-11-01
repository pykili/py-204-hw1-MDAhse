a = ''
n = 0
while n < 10:
	a = a + input()
	n = n + 1
alphabet = a[0]
for i in a:
	if i not in alphabet:
		alphabet = alphabet+i
print('алфавит: ',alphabet)
