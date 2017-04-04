'''PROGRAM TO PRINT THE FOLLOWING PATTERN
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
'''

#--- main ---
n=int(input("ENTER THE MAXIMUM NUMBER OF STARS YOU WANT :: "));   #INPUT
for i in range(n):          #INCREASING STARS
    for j in range(i):  
        print ('* ', end="")  
    print('')  
  
for i in range(n,0,-1):     #DECREASING STARS
    for j in range(i):  
        print('* ', end="")  
    print('')

QUIT=input("PRESS ENTER TO EXIT")
