def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd






lst=[56,67,89,34,68,88,43,67,99,23,67]
even,odd=count(lst)

print(even)
print(odd)
