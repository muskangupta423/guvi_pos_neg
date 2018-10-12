N,K=input("Enter value of N and k").split()
sum=0
lst=[int(n) for n in input().split()]
for i in range(0,int(K)):
	sum=sum+lst[i]
print(sum)