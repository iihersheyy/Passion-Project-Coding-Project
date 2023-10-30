#Fibonacci Sequence : 0, 1, 1, 2, 3, 5, 8 ..... n terms

def fib(n):

    if n==0:
        return 0 
    
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print("\n Fib of 10 : ")
for i in range(10):
    print(fib(i))