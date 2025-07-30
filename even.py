n=int(input("enter the no element in the list"))
list=[]
even=[]
for i in range(n):
    n=int(input("enter the element in the list"))
    list. append(n)
    if n % 2==0:
        even.append(n)
print(list)
print("Even numbers:",even)