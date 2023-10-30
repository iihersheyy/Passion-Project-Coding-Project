#Problem : Constructing decreasing Pyramid 
'''
       !
      !!!
     !!!!!
    !!!!!!!
   !!!!!!!!!
  !!!!!!!!!!!
 !!!!!!!!!!!!!
!!!!!!!!!!!!!!!
'''

for i in range(1,10):
    for j in range(1,10-i):
        print(" ",end='')
    for i in range(1,i):
        print("!",end='')
    for k in range(i,1,-1):
        print("!",end='')
    print("")