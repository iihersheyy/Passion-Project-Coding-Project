#Problem : searches for a specific word in a text file and returns the number of occurrences.

import re

search_string = "sis"

try:
    with open("./welcome.txt","r") as fp:
        content = fp.readline()
        word = 0
        while(content):
            word += len(re.findall(search_string,content))
            content = fp.readline()
    print(" '%s' is FOUND %d times in the file " % (search_string,word) )
except Exception as e:
    print("File read operation failed")
    
    