from funcstools import reduce
nums=[3,4,6,85,4,32,7,89,9,86]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)

doubles=list(map(lambda n:n*2,evens))
print(doubles)

add=reduce(lambda a,b:a+b,doubles)
print(add)
