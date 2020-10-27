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
# вы сказали, что если я не хочу везде заменять каунт, чтобы я отдельно программку написала, так что вот она!
word = input("введите слово ")
s = input("введите символ ")
n = 0
for i in word:
  if i in s:
    n = n+1
print(n)
