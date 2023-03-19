from sellerSection import SellerSecion
seller = sellerSection()

print(" welcome to seven city foodcity")
print(" enter number to access to system")
print(" system\n 1) type 1: enter to shop management \n  2) type 2 : enter to custemer section")

number = int(input("enter the number :"))

while True:
    if (number ==1):
        user_name = input("enter user name: ")
        password = input("enter password : ")
        while True:
            if (user_name == "hello123" and password == "shop"):
                print("welcome to seller sction!")
                seller.run()
                 break
            else:
                user_name = input("enter user name : ")
                password = input("enter password : ")
    elif(number == 2):
        print("hello cutemor!")
        number = int(input("enter number : "))
    elif (number ==3):
        print("thnaks for comng have a good day")
        quit() #meken weradi ekak gauwama quit wenawa
    else:
        print("invalid responsce")
        number =int(input("enter numbr : "))
         
        
                
          
          
    
  
  
