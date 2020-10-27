front_vow = "eiöü"
back_vow = "aıou"
net = 0
da = 0
n = 0
while n < 10:
	line = input()
	if line=='':
		n=n
	elif line[0]=='#':
		n=n
	else:
		k=0
		l=0
		p=0
		g=0
		while k<len(line):
			if line[k]=='\t' and l == 0:
				l=k
			elif line[k]=='\t' and l != 0 and p == 0:
				p=k
			elif line[k]=='\t' and l != 0 and p != 0 and g ==0:
				g=k
			k=k+1
		lemma = line[p+1:g]
		wordform = line[l+1:p]
		if wordform!= lemma and (p-l < g-p and lemma == wordform[0:g-p-1]):
				e=0
				s = 0
				z = 0
				while e < 4:
					if back_vow[e] in lemma:
							s = s+1
					elif front_vow[e] in lemma:
							z = z + 1
				if s==0 or z==0:
					da = da + 1
				else:
					net = net + 1
		n = n + 1
print('нет:',net)
print('да:',da)
