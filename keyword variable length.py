def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
        


person('aniket',age=21,city='pune',mob=8790)              
