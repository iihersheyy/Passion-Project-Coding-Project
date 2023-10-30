#Problem : Encry the given file

import re
try:
    with open("./welcome.txt","r") as fp:
        content = fp.readlines()
        encry = ""
        with open("./encry.txt","w+") as tp:
            
            for i in content:
                for j in range(len(i)):
                    encry = encry + chr(ord(i[j])+23)

            tp.write(encry)

            fp.close()
            tp.close()

    print("Actual Contnet : \n %s" % content)
    print("Encrypt Contnet : \n %s" % encry)
    
except Exception as e:
    print("File read operation failed %s" % e)
    
    