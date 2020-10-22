user_input = input()
b = user_input[0]
for i in user_input:
	if i not in b:
		b = b+i
n = 0
c = ''
for i in b:
	if user_input.count(i) > n:
		n=user_input.count(i)
		c = i
print(c)
