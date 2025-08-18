even=[]
l=[]
n=int(input("Enter limit"))
for i in range(n):
    s=int(input("Enter number"))
    l.append(s)
    if s%2==0:
        even.append(s)
print("List of even numbers:",even)