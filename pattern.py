"""for i in range(4):
    print()
    for j in range(4):
        print('#',end="")
        
for i in range(5):
    print(i*'#')
    for j in range(0):
        print('#',end='')
    
        
 ############3             
for i in range(1,5):
    for j in range(1,5):
        print('#',end="")
    print('')
    
#####################

for i in range(1,5):
    for k in range(1,i+1):
         print('#',end="")
    print('')
        
print(' ') #space k liye

################
for i in range(1,6): # i vertically 5 baar print karega 
    for k in range(1,6-i):
         print('#',end="")
    print('')
"""

num= input('enter odd length no')
length=len(num)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
