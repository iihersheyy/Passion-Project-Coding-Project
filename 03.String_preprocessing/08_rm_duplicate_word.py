#Problem : Remove the duplicate word in the string

my_string = "Welcome to python to day, Welcome to string function"


output = ""
for i in my_string.split():
    if i not in output:        
        output = output + ' ' + i

print("Orginal String                        : %s" % my_string)
print("After removal of the duplicate String : %s" % output)
