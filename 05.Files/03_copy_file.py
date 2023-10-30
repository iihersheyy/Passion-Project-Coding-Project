#Problem : Write following sequence into a txt file
'''
1
11
111
1111
11111
111111
1111111
11111111
111111111
'''

try:
    with open("./my_file.txt","r") as fp:
        content = fp.read()

        with open("./my_target.txt","w") as tp:
            tp.write(content)
    
    tp.close()
    fp.close()
    
except Exception as e:
    print("File opeation failed")