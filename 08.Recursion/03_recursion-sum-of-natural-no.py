
#fun(n) = n + fun(n-1)
#fun(1) = 1 
#fun(5) = 5 + fun(5-1)
#           + 4 + fun(4-1)
#               + 3 + fun(3-1)
#                   + 2 + fun(2-1)
#                       + 1 

def add(n):
    if n == 1:
        return 1
    else:
        return n * add(n-1)

print("\nFirst 5 natual number sum using recurssion : %s " % (add(5)))
print("\nFirst 10 natual number sum using recurssion : %s " % (add(10)))
print("\nFirst 3 natual number sum using recurssion : %s " % (add(3)))