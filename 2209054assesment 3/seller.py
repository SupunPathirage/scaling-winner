form billprnt import Bill
form productupdate import product
import datetime

class SellerSection:
    def __init__(self):
        self.seller = ["kamal','silva"]
    def run(self):
        print("###----Welcome Seller Section---###")

        while True:
            print("Enter Number toaccess to system")
            print("Seller Tasks \n 1) Type 1: Create new bill \n 2) Type 2: Add new item \n 30 Type 3: Update Quantity\nn 4) type 0: GO BACK")
            number =int(input("eNTR NUMBER:"))
            print("###----- loading----###\n")
            if (number ==1):
                self.task1()
            elif (number==2):
                self.task2()
            elif (number ==3):
                self.task3()
            elif (number ==0):
                break
            else:
                print("###----invalid nput---##3")

     def getAllProducts(self):
         print("Available products and Unit pric(Rs)")
         productPrieLis = []
         with open('price.txt' , 'r') as file:
             for line in file:
                 temp = line.strip()
                 productPriceLis.append(temp)
                 
         return productPriceLis

    def displayTotal(self,pNames,oQuantity,products):
        prouctList = pNames
        unitPrices = []
        item = 0
        for p in prouctList:
            for oneP in products:
                if(p in oneP):
                    unitP = int(oneP.split(" ")[1])
                    unitPrices.append(unitP)
                    productRemove = product(p,unitP)
                    productRemove.autoUpdateQuantity(oQuantity[item])
             item +=1

             today = str(datatime.datatime.now())
             bill = Bill(today,productlist,unitPrices,oQuantity)
             bill.getTotal()
             print("To Print Bill")
             paid = int(input("Enter paid amount"))
             bill.printBill(paid)
             print("\n")

    def createBill(self,orderList,products):
        pName = []
        oQuantity = []
        total = 0
        for value in orderList:
            if(value == "#"):
                break
            n = value.split(" ")
            pNames.append(n[0])
            oQuantity.append(int(n[1]))
        if(len(pNames) == 0):
            return "No Item Selected"
        self.displayTotal(pNames,oQuantity,products)

    def task1(self):
        products = self.getAllProducts()
        print("####-------Create New Bill------------####")
        print("Enter:Product_Name Ordered_Quantity")
        itemList =[]
        getTotal =' '
        i=1
        while (getTotal !="#"):
        print("ADD ITEM PRES \" 1 \" AND GET TOTAL PRESS \" # \"")
        getTotal = input("PRESS :")
        if getTotal == "1":
            item = input("Quantity : ")
            qy = input("Quantity :")
            itemList.append(item+""+qy)
            print("ADDED SUCCES")
        else:
            itemList.append(getTotal)
        i += 1
    print(itemList)
    self.createBill(itemList,products)

def addNewItem(self,productName,unitPrice,stock):
    prod = product(productName,unitPrice,stock):
    proud.manuallyUpdateQuantity(stock)
    print("###-----New Item added ssuccess---####")
    print("\n")
    
def task2(self):
    print("###3----Add New Items------#####3")
    name = input("Enter product name: ")
    uPrice = int(input("Enter unit price: "))
    stock = int(input("EnterQuantity: "))
    self.addNewItem(name,uPrice,stock)

def updateaddStock(self,productName,unitPrice,stock):
    prod = product(productName,unitPrice):
    proud.manuallyUpdateQuantity(stock)
    print("###-----stock update success---####")
    print("\n")
    
def updateremoveStock(self,productName,unitPrice,stock):
    prod = product(productName,unitPrice):
    proud.autoUpdateQuantity(stock)
    print("###-----stock update success---####")
    print("\n")

def task3(self):
    print("###----Update stock---####")
    name = input("Enter product name: ")
    uPrice = int(input("Enter unit price: "))
    stock= int(input("Enter Quantity: "))
          


def run(self):
    print("####------Welcome Seller Section----####")

    while True:
        print("Enter Number to access to system")
        print("Seller Tasks \n 1) type 1: Create ew bill \n 2) Type 2 all")
        number = int(input("Enter number :"))
        print("###------loading-----------\n")
        if (number == 1):
            self.task1()
        elif (number == 2):
            self.task2()
        elif (number == 3):
            self.task3()
        elif (number == 0):
            break
        else:
            print("####------invalid input----####")
            
    
        
    
        
        
                
                
            
