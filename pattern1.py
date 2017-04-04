'''PROGRAM TO PRINT THE FOLOWING PATTERN
*
* *
* * *
* * * *           '''

#--- main ---
x=int(input("HOW MANY STAR(*) LINES SHOULD BE PRINTED? :: "))
for i in range(0,x):
    for j in range(0,i+1):
        print("* ",end="")
    print()
