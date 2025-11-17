print("Enter the vectors:")

a=int(input("Enter i component of 1st vector: "))
b=int(input("Enter j component of 1st vector: "))
c=int(input("Enter k component of 1st vector: "))

x=int(input("Enter i component of 2nd vector: "))
y=int(input("Enter j component of 2nd vector: "))
z=int(input("Enter k component of 2nd vector: "))

if a/x==b/y and a/x==c/z and b/y==c/z:
	print("Parallel")
print("Dot product = ", (a*x)+(b*y)+(c*z))

