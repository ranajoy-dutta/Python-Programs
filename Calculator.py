''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

# define functions
    
def add(x, y):    
   """This function adds two numbers"""
   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""
   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""
   return x * y

def divide(x, y):
   """This function divides two numbers"""
   return x / y


# take input from the user
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5. Enum1it")
    choice = input("Enter choice(1/2/3/4/5):")
    
    if choice == '1':
         num1 = int(input("Enter first number: "))
         num2 = int(input("Enter second number: "))
         print(num1,"+",num2,"=", add(num1,num2))
       
    
    elif choice == '2':
       num1 = int(input("Enter first number: "))
       num2 = int(input("Enter second number: "))
       print(num1,"-",num2,"=", subtract(num1,num2))
    
    elif choice == '3':
            
       num1 = int(input("Enter first number: "))
       num2 = int(input("Enter second number: ")) 
       print(num1,"*",num2,"=", multiply(num1,num2))
    
    elif choice == '4':        
       num1 = int(input("Enter first number: "))
       num2 = int(input("Enter second number: "))
       print(num1,"/",num2,"=", divide(num1,num2))
       
    elif choice == '5':
        break
    else:
       print("Invalid input")
    print("="*50,"\n")
    
     
            
