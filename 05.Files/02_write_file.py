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
    with open("./my_file.txt","w") as fp:
        for i in range(10):
            for j in range(i):
                fp.write("1")
            fp.write("\n")

    fp.close()
    with open("./my_file.txt","r") as fp:
        print(fp.read())
    fp.close()
    
except Exception as e:
    print("File opeation failed")