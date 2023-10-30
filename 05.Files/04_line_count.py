#Problem : Find number of lines in the file

try:
    with open("./welcome.txt","r") as fp:
        content = fp.readlines()
        print("Number of lines : %d" % len(content))
except Exception as e:
    print("File read operation failed")
    
    