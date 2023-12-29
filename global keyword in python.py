a=110
print(id(a))

def something():
    a=9
    x=globals()['a']
    print(id(x))

    print("in func",a)
    globals()['a']=15


something()    

print(a)
