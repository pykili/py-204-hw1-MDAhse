user_input = input()
alphabet = user_input[0]
for i in user_input:
	if i not in alphabet:
		alphabet = b+i
print(alphabet)
