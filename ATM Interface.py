print("Welcome to State bank of India")
p=int(input("Enter your pin number: "))
m = 50000
if(p!=0): 
 print("1-Check Balance")
 print("2-Deposit")
 print("3-Withdraw")
 
c = int(input("Please choose transactions: "))

if(c==1):
    print("Your Account Balance is : ",m)
    
elif (c == 2):
    d = int(input("Enter the amount to be deposited: "))
    if (d>0):
        print(d, "is successfully deposited")
        print("The Available Balance is : ",m+d)
    else:
        print("The amount is not Deposited")      
    
elif (c == 3):
   w=int(input("Enter the amount to be withdrawn: "))
   if (w < m):
      print(w, "is withdrawn successfully")
      print("The Available Balance is : ",m+w)
   else:
      print("The amount is not Withdrawn")

else:
    print("Wrong choice")
