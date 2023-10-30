#Problem : Find start/end index of a word in given string in all occurrance 

import re
my_string = "Hello World, World is beatiful, which is why we are here"

for i in re.finditer("is",my_string):
    print(i.span())