n=1
while n <= 100:
	k = 1
	s = 0
	while k <= (2*n - 1):
		s = s + k
		k = k + 2
	if s == n**2:
		print("Для",n,"выполняется")
	else:
		print("Для",n,"не выполняется")
	n = n + 1
