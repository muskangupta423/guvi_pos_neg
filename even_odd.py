a = input("Enter the number:")
if a.isdigit():
	if int(a)%2==0:
		print("Even")
	else:
		print("Odd")
else:
    print("Invalid")