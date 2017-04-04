''' PROGRAM TO IMPLEMENT INSERTION SORT '''

def insertionSort(alist):            #FUNCTION FOR INSERTION SORT
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue

#--- main ---
n=int(input("ENTER THE LENGTH OF LIST :"))          #INSERTING ELEMENTS
print ("\n ENTER ELEMENTS FOR LINEAR LIST \n")
ar=[0]*n
for i in range(n):            #ARRAY_INPUT
       ar[i]=int(input("ELEMENT "+str(i+1)+":"))
print("ARRAY BEFORE SORTING :: ",ar)       
insertionSort(ar)   #SORTING
print("ARRAY AFTER SORTING :: ",ar)           #OUTPUT

QUIT=input("PRESS ENTER TO EXIT")
