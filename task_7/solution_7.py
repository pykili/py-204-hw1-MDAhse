line = input()
is_palindrom = True
n=0
while n<len(line)/2:
	if line[n]!=line[len(line)-1-n]:
		is_palindrom = False
		
	n = n+1
print(is_palindrom)
