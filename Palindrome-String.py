""" PROGRAM TO CHECK WHETHER GIVEN STRING IS PALINDROME OR NOT """

my_str = input("ENTER THE STRING :: ")          #Taking Input from User

my_str = my_str.casefold()               # Making it suitable for Caseless comparison
rev_str = reversed(my_str)               # Reversing the string using function

if list(my_str) == list(rev_str):
   print("It's a Palindrome")
else:
   print("It's not a Palindrome")

QUIT= input("\nPRESS ENTER TO EXIT")

