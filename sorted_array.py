N=(input())
if(N.isdigit() and int(N)<=1000 and int(N)>0):
	li=list(map(str,input().split()))
	for i in range(len(li)):
		if(li[i].isalpha()):
			print('Invalid')
			exit()		
	li.sort()
	for i in li:
		print(i,end=' ')
else:
	print('Invalid')
	exit()	