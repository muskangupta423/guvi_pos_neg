#tofind odd numbers between interval a and b
a,b=input("Enter the two numbers").split()
for i in range(int(a)+1,int(b)):
	if i%2!=0:
		print(i,end=" ")