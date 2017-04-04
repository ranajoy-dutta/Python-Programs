''' PROGRAM TO PRINT THE FOLLOWING PATTERN
      *
     * *
    * * *
   * * * *
  * * * * *              '''

#--- main ---
k = 0
rows=int(input("HOW MANY STAR(*) LINES SHOULD BE PRINTED? :: "))
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()

quit1=input("PRESS ENTER TO EXIT")
