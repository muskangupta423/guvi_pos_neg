a,b=(input("enter both numbers").split(" "))
if(a.isdigit() and b.isdigit()):
	for i in range(int(a)+1,int(b)):
		j=i
		s=0
		while(j>0):
			r=j%10
			s+=r**3
			j=j//10
		if(s==i):
			print(i)
		else:
			pass
else:
	print("Invalid")