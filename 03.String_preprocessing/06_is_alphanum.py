#Problem : Check whether given string is alpha numeric or not ?

my_string = "Welcome2323"

#my_list = ['A','Z','a','z','1','9','0']
#for i in my_list:
#    print(i, ord(i))

isalpha = '0'
for i in range(len(my_string)):
    if ( ord(my_string[i]) >= 65 and ord(my_string[i]) <= 90 ) or \
        ( ord(my_string[i]) >= 97 and ord(my_string[i]) <= 122 ) or \
            ( ord(my_string[i]) >= 48 and ord(my_string[i]) <= 57 ):
        isalpha='1'
    else:
        isalpha='0'
        break

if isalpha == '0':
    print("%s - Not a alphanumberic" % my_string)
else:
    print("%s - Is a alphanumberic" % my_string)
