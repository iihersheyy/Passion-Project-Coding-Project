#Problem : Error handling 


# Example1 : ZeroDivisionError handling 
a = 10
b = 0
#print(a/b) >>> This will give {ZeroDivisionError: division by zero } error

# Example2 : Any Exception handling 
a = "1"
b = 0

try :
    print(a/b)
except ZeroDivisionError:
    print("Error : Denominator cannot be Zero")
except Exception:
    print("Error : Unable to perform divison")