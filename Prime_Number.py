'''PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS PRIME OR NOT'''

num = int(input("ENTER THE NUMBER : "))   #INPUT

if num > 1:                                                                         # prime numbers are greater than 1
   for i in range(2,num):           # CHECK FOR FACTORS
       if (num % i) == 0:
           print (num,"IS NOT A PRIME NUMBER")
           print ("REASON :: ",i,"TIMES",num//i,"IS",num)
           break
   else:
       print (num,"IS A PRIME NUMBER")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print (num,"IS NOT A PRIME NUMBER")

K=input("\n *** PRESS ENTER TO EXIT ***")

