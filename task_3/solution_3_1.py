user_input = input()
b = user_input[0]
for i in user_input:
	if i not in b:
		b = b+i
print(b)
