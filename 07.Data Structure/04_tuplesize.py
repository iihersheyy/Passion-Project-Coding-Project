#Problem : Find the size of the Tuple 
#In Python, a tuple is an ordered, immutable collection of elements. This means that once you create a tuple, 
#you cannot change its contents (add, remove, or modify elements) unlike lists, which are mutable.

import os 

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))
 
print("Tuple-1 Size : %s Bytes" % Tuple1.__sizeof__())
print("Tuple-2 Size : %s Bytes" % Tuple2.__sizeof__())
print("Tuple-3 Size : %s Bytes" % Tuple3.__sizeof__())
