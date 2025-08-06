tuple_list=[(2,1),(3,6),(9,8),(4,7)]
n=len(tuple_list)
for i in range(n):
    for j in range(0,n-i-1):
        if tuple_list[j][1]>tuple_list[j+1][1]:
            tuple_list[j],tuple_list[j+1],tuple_list[j+1],tuple_list[j]
print("sorted list based on second element :")
print(tuple_list)