def isempty(stk):
       if stk==[]:
              return True
       else:
              return False

def Push(stk, item):
       stk.append(item)
       top=len(stk)-1

def Pop(stk):
       if isempty(stk):
              return "underflow"
       else :
              item=stk.pop(0)
              if len(stk)==0:
                     top=None
              else:
                     top=len(stk)-1
       return item

def Peek(stk):
       if isempty(stk):
              return "underflow"
       else:
              top=len(stk)-1
              return stk[top]

#--- main ---
stack=[]
top=None
while True:
       print ("STACK OPERATIONS")
       print ("1. Push")
       print ("2. Pop")
       print ("3. Peek")
       print ("4. Exit")
       ch=int(input("\nEnter your choice :: "))
       if ch==1:
              item=int(input("Enter Item :"))
              Push(stack,item)
              print("*** Element Inserted ***")
       elif ch==2:
              item=Pop(stack)
              if item=="underflow":
                     print ("*** Underflow! Stack is empty ***")
              else:
                     print ("*** Popped item is ",item," ***")
       elif ch==3:
              item=Peek(stack)
              if item=="underflow":
                     print ("*** Underflow! Stack is empty ***")
              else:
                     print ("*** Topmost item is",item," ***")
       elif ch==4:
              break
       else:
              print ("\tInvalid Choice!!!")
       print("="*50,"\n")
       
