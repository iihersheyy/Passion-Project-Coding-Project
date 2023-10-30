#Problem : To use variable length parameters in the function 

def add(*args):
    result = 0 
    for num in args:
        result += num 

    return result

print("Call with 3 command line parameter : %d" % add(1,2,3))
print("Call with 2 command line parameter : %d" % add(11,22))
print("Call with 5 command line parameter : %d" % add(10,20,30,40,50))