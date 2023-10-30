#Problem : Decrypt the given file

import re
try:
    with open("./encry.txt","r") as fp:
        content = fp.readlines()
        encry = ""
        with open("./clear.txt","w+") as tp:
            
            for i in content:
                for j in range(len(i)):
                    encry = encry + chr(ord(i[j])-23)

            tp.write(encry)

            fp.close()
            tp.close()

    print("Encrypt Contnet : \n %s" % content)
    print("Decrypt Contnet : \n %s" % encry)
    
except Exception as e:
    print("File read operation failed %s" % e)
    
    