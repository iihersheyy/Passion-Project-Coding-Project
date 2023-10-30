#Problem : In the given string, remove one character from first to last

my_string = "Welcome"
#Expected output = "elcome","Wlcome","Wecome","Welome","Welcme","Welcom"

parts = []
for i in range(len(my_string)+1):
    parts += [(my_string[:i],my_string[i:])]

for i,j in parts:
    print(i+j[1:])