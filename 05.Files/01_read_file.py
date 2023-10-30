#Problem : Read the content of the file

file_name ="./welcome.txt"

try:

    with open(file_name,"r") as fp:
        print(fp.read())

except Exception as e:
    print("File reading error %s " % e)