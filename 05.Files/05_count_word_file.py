#Problem : Find number of words and character in the file
import re
try:
    with open("./welcome.txt","r") as fp:
        content = fp.readline()
        word = 0
        while(content):
            word += len(re.findall("\w+",content))
            content = fp.readline()
    print("Number of words : %d " %word )
except Exception as e:
    print("File read operation failed")
    
    