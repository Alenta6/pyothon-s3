m=int(input("enter the starting number (m): "))
n=int(input("enter the ending number (n): "))
squareset={x**2 for x in range(m, n+1) if x % 2 ==0}
print("set of squares of even numbers between {m} and {n}:")
print(squareset)