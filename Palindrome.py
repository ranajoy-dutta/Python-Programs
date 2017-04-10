# PROGRAM TO CHECK WHETHER GIVEN INPUT IS PALINDROME OR NOT

#---main---
my_str = input("ENTER THE STRING :: ")

my_str = my_str.casefold()    # make it suitable for caseless comparison
rev_str = reversed(my_str)    #reversing the string

if list(my_str) == list(rev_str):
   print("\nIT IS A PALINDROME")
else:
   print("\nIT IS NOT A PALINDROME")

QUIT= input("\nPRESS ENTER TO EXIT")
