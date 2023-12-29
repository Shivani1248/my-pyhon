pos=-1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list=[0,7,8,5,4,3,7,8]
n=7
if search(list,n):
    print("found at",pos+1)
else:
    print("not found")
