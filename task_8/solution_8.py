N = int(input())
k=1
a = int(input())
s=a
while (a!=0 and k<N):
	a = int(input())
	s = s + a
	k = k + 1
	
print(s/k)
