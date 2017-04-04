"""BINARY SEARCHING IN AN ARRAY"""
def Bsearch(ar,item):       #FUNCTION FOR LINEAR SEARCH
       beg=0
       last=len(ar)-1
       mid=(beg+last)//2
       for i in range (beg,last):
              print("rount ",i)
              if (ar[mid]>item):
                     last=mid-1
              elif (ar[mid]<item):
                     beg=mid+1
              else :
                     return mid


# --- main---
n=int(input("ENTER THE LENGTH OF LIST :"))
print ("\n ENTER THE ELEMENTS :: \n")
ar=[0]*n
for i in range(n):            #ARRAY_INPUT
       ar[i]=int(input("ELEMENT "+str(i+1)+":"))
item=int(input("ENTER THE ELEMENT TO BE SEARCHED:"))
if ar[0]==item:
       print ("\n ELEMENT : ",item," \n FOUND AT POSITION : 1") #OUTPUT
else:
       index=Bsearch(ar,item)
       if index:
              print ("\n ELEMENT : ",item," \n FOUND AT POSITION :", (index+1)) #OUTPUT
       else:
              print ("\n SORRY !! GIVEN ELEMENT COULD NOT BE FOUND \n")     #OUTPUT

k=input("\n *** PRESS ENTER TO EXIT ***")
