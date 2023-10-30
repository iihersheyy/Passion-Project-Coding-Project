#Problem : Example of deafult argument

def add2(x=10,y=20):
    return(x+y)

print("Call add2 without any args : %d" % add2())
print("Call add2 with single arg : %d" % add2(1))
print("Call add2 with 2 args : %d" % add2(1,3))