#Problem : Get userid,mail-server,domain-type from the given email id

import re

my_mail = "samj2004@gmail.com"

result = re.search("([A-Za-z0-9]+)@([\w]+\.([\w]+))",my_mail)
print("Mail-id : %s" % result.group(1))
print("Mail Server : %s" % result.group(2))
print("Domain Name : %s" % result.group(3))