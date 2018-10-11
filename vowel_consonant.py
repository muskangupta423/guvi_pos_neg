a = input("Enter the character:")
if(len(a)>1):
	print("Invalid")
else:
	if a in 'aeiouAEIOU':
		print("Vowel")
	elif a in '!@#$%^&*()_+=-:;?/."<>|{}[]':
		print("Invalid as they are special characters")
	else:
		print("Consonant")