
with open("romeo.txt","r") as File1:

	file_stuff = File1.read()
	print(file_stuff)

print(File1.close())
print(file_stuff)