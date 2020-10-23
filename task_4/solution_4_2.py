n = 0
while n < 10:
	c = input()
	if c=='':
		n=n
	elif c[0]=='#':
		n=n
	else:
		k=0
		l=0
		p=0
		g=0
		while k<len(c):
			if c[k]=='\t' and l == 0:
				l=k
			elif c[k]=='\t' and l != 0 and p == 0:
				p=k
			elif c[k]=='\t' and l != 0 and p != 0 and g ==0:
				g=k
			k=k+1
		if c[l+1:p]!= c[p+1:g] and (p-l-1 < g-p-1 or c[p+1:g] != c[l+1:l+g-p]):
				print(c[l+1:p])
				print(c[p+1:g])
		n = n + 1
