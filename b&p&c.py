av=10
x=int(input("enter a no of candies do u want"))
i=1
while i<=x:
    if i>av:
        break
        
    print("candy")
    i=i+1
print("bye")


for i in range(1,100):
    if i%2!=0:
        pass
    
    else:
        print(i)

        
for i in range(1,100):
    if i%3==0 and i%5==0:
        continue
    print(i)

print("bye")
