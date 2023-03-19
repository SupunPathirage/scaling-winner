class product:
     def __init__(self,productName):
         self.productName = productname
     def __init__(self,productName,unitPrice):
         self.productName = productName
         self.unitprice = unitprice
     def __init__(self,productName,unitPrice,quantity):
         self.productName = productName
         self.unitPrice = unitPrice
         self.quantity = quantity

     def autoUpdateQuantity(self,boughtQuantity):
         productList = []
         productQuantity = []
         with open("product.txt", "r") as file:
             for line in file:
                 product,quantity = line.strip().split(" ")
                 productList.append(product)
                 productQuantity.append(quantity)

             if self.productName in productList:
                 if (int(productQuantity[productList.index(self.productName)])-boughtQuantity) >= 0:
                     productQuantity[productList.index(self.productName)] = (int(productQuantity[productList.index(self.productName)])-boughtQuantity)
                 else:
                     print("this quantity can not be supply.")
             else:
                  print("out of stock")
                  
         with open("product.txt","w") as file:
            for i in range(len(productList)-1):
                file.write(productList[i]+" "+str(productQuantity[i])+"\n")
            else:
                file.write(productList[-1]+" "+str(productQuantity[-1]))
                
     def manuallyUpdateQuantity(self,boughtQuantity):
          productList = []
          productQuantiy = []
          productPrice= []

          with open("product.txt","r") as file:
              for line in file:
                 product,quantity = line.strip().split(" ")
                 productList.append(product)
                 productQuantity.append(quantity)

            if self.productName in productList:
                productQuantity[productList.index(self.productName)] = (int(productQuantity[productList.index(self.productName)]) + boughtQuantity)
           else:
               with open("price.txt") as file2:
                   for line in file:
                       product,price = line.strip().split(" ")
                       productPrice.append(int(price))

           if self.productName in productList:
                with open("product.txt","w") as file3:
                    for i in range(len(productList)-1):
                         file.write(productList[i]+" "+str(productQuantity[i])+"\n")
                    else:
                         file.write(productList[-1]+" "+str(productQuantity[-1]))
            else:
                with open ("product.txt","w") as file4:
                    for i in range(len(productList)):
                        file4.write(self.productName+" "+str(productQuantity[i])+"\n")
                    else:
                        file4.write(self.productName+" "+str(boughtQuantity))
                 with open ("product.txt","w") as file5:
                    for i in range (len(productList)):
                        file4.write(self.productName+" "+str(productPrice[i])+"\n")
                    else:
                        file4.write(self.productName+" "+str(self.unitPrice))
                

                
                        
                 
                
                 
                 
                 

   
