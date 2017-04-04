"""LINEAR SEARCHING IN AN ARRAY"""
def Lsearch(ar,item):       #FUNCTION FOR LINEAR SEARCH
       i=0
       while i<len(ar) and ar[i]!=item:   #TRAVERSING
              i+=1
       if i<len(ar): 
              return i
       else:
              return false

# --- main---
n=int(input("ENTER THE LENGTH OF LIST :"))
print ("\n ENTER ELEMENTS FOR LINEAR LIST \n")
ar=[0]*n
for i in range(n):            #ARRAY_INPUT
       ar[i]=int(input("ELEMENT "+str(i+1)+":"))
item=int(input("ENTER THE ELEMENT TO BE SEARCHED:"))
if ar[0]==item:
       print ("\n ELEMENT : ",item," \n FOUND AT POSITION : 1") #OUTPUT
else:
       index=Lsearch(ar,item)
       if index:
              print ("\n ELEMENT : ",item," \n FOUND AT POSITION :", (index+1)) #OUTPUT
       else:
              print ("\n SORRY !! GIVEN ELEMENT COULD NOT BE FOUND \n")     #OUTPUT

k=input("\n *** PRESS ENTER TO EXIT ***")
