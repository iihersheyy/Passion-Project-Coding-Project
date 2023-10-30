#Problem : Convert the given string into title case

my_string = "welcome to python"

#A 65
#Z 90
#a 97
#z 122

output = ""
for i in my_string.split():
    if ( ord(i[0:1]) >= 97 and ord(i[0:1]) <= 122 ) :
        output = output + ' ' + chr(ord(i[0:1])-32)+i[1:]
print("Actual String     : %s" % my_string)
print("Title case String : %s" % output)
        
