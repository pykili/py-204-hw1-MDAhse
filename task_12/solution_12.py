line = input()
occurred_twice = False
n = 0
while n < len(line)-1:
	k =0
	bi = line[n:n+1]
	k = line.count(bi)
	if k >=2:
		occurred_twice = True
	n = n + 1
print(occurred_twice)
