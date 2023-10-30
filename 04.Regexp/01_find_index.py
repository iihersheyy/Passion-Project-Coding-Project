#Problem : Find the search string index from the given string
#Given String : Welcome to Fremont
#Search String : Fremont
#Output : 11 17

import re
my_string = "Welcome to Fremont"
search_string = "Fremont"
result = re.search("Fremont", my_string)
print(result.span())
print(result.start())
print(result.end())