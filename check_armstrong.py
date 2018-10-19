n=(input("enter number"))
s=0
if(n.isdigit() and int(n)<100000):
	l=len(n)
	n=int(n)
	j=n
	while(n>0):
		r=n%10
		s+=r**l
		n=n//10
	if(j==s):
		print('YES')
	else:
		print('No')
else:
	print('Invalid')