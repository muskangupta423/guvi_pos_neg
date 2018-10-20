n=(input())
if(n.isdigit() and int(n)<=1000 and int(n)>0):
	l=list(map(str,input().split()))
	for i in range(len(l)):
		if(l[i].isalpha()):
			print('Invalid Input')
			exit()		
	l.sort()
	n=int(n)
	if(int(n)%2!=0):
		print(l[(n//2)])
	else:
		print(l[(n//2)-1])	
else:
	print('Invalid Input')
	exit()	