front_vow = "eiöü"
back_vow = "aıou"
net = 0
da = 0
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
		if c[l+1:p]!= c[p+1:g] and (p-l < g-p and c[p+1:g] == c[l+1:l+g-p]):
				e=0
				s = 0
				z = 0
				while e < 4:
					if back_vow[e] in c[p+1:g]:
							s = s+1
					elif front_vow[e] in c[p+1:g]:
							z = z + 1
				if s==0 or z==0:
					da = da + 1
				else:
					net = net + 1
		n = n + 1
print('нет:',net)
print('да:',da)

