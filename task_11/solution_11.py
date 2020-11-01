line = input()
isin=True
k=0
n=0
left = ''
right = ''
while line[k]!= ' ':
	left = left + line[k]
	k = k + 1
	n = n + 1
right = line[n+1:len(line)-1]
s = 0
p = 0 
if len(left)<= len(right):
	while s < len(left):
		if left[s]!=right[p]:
			isin = False
		s = s +1
		p = p + 1
else:
	isin = False
print(isin)
