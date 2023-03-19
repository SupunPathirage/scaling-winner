class Bill:
    def __init__(self,date,productList,unitPrice,quantity):
        self.date = date
        self.productList = productList
        self.unitPrice = unitPrice
        self.quantity = quantity

    def billHeader(self):
         print("+---------------------------------------------------------------+")
         print("------------------FOODCITY---------------------------------------")
         print("+---------------------------------------------------------------+")
         print("------------------------Date:{:35s} ".format(self.date)) #"2022/05/05 8:42:23" (:35 change karatheki ehata mehata :39,:40)meeken wenne uda print line wlin pita noyana eka

            
    def billFooter(self):
         print("+---------------------------------------------------------------+")
         print("---------------THANK YOU COME AGAIN------------------------------")
         print("+---------------------------------------------------------------+")
         
    def getTotal(self):
         l =len(self.productList)
         total = 0
         for value in range(l):
            total += self.unitPrice[value]*self.quantity[value]
         return (total)
    
    def createBill(self,paid):
         l=len(self.productList)
         self.billHeader()
         print("+---------------+----------------+----------------------------+--")
         print(" name                   ouanty              price                ")
         print("+---------------------------------------------------------------=")
         for value in range(l):
             subTot = self.unitPrice[value] * self.quantity[value]
             print(" {:16s} {:14s} {:12s} ".format(self.productList[value]," "+str(self.quantity[value])," "+str(subTot)))
             print("+-----------------------------------------------------------+")
         print("Total Bill is Rs. {:34s}".format(str(self.getTotal ())))
         print("+---------------------------------------------------------------+")
         print("Balance :Rs{:32s}".format(str(paid - self.getTotal ())))
         print("+---------------------------------------------------------------+")
         self.billFooter()

productList = ["mando","apple","banna"]
unitPrice = [12,15,10]
quantity = [40,30,15]

bill = Bill("2022/005/05 21:23:37",productList,unitPrice,quantity)
print("Total price is : Rs "+ str(bill.getTotal()))
paid = int(input("Bill payment : Rs "))
bill.createBill(paid)



        
