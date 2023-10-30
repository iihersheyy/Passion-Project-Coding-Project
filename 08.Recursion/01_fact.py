#Factorial of 5 = 5 * 4 * 3 * 2 * 1 

#  n * face(n-1)
# fact(1) = 1 

#  5 * fact(4) 
#    * 4 * fact(3)
#        * 3 * fact(2)
#            * 2 * fact(1)
#            * 2 * 1


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

for i in range(1,10):
    print("Fact(%s) : %s" % (i,fact(i)))