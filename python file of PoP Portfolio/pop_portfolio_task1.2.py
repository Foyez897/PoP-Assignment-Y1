# Task1.2

class StockItem:
    #Class variable
    stockCategory = 'Car accessories'
    
    def __init__(self, stockCode, quantityInStock, priceWithoutVAT):
       #private variables 
       self.__stockCode = stockCode
       self.__quantityInStock = quantityInStock
       self.__priceWithoutVAT = priceWithoutVAT
    
    #Geters & setters
    def get_stockCode(self):
        return self.__stockCode
    
    def get_quantityInStock(self):
        return self.__quantityInStock
    
    def set_quantityInStock(self, quantityInStock):
        if quantityInStock > 0 and quantityInStock <= 100:
            self.__quantityInStock = quantityInStock
        else:
            print("Invalid quantityInStock. Quantity shoudl be between 1 and 100.")

    def get_priceWihoutVAT(self):
        return self.__priceWithoutVAT

    def set_priceWithoutVAT(self, price):
        self.__priceWithoutVAT = price

    def get_priceWithVAT(self):
        VATrate = self.get_VAT() / 100
        return self.__priceWithoutVAT * (1 + VATrate)
    
    def get_stockName(self):
        return "Unknown Stock Name"
    
    def get_stockDescription(self):
        return "Unknowm Stock Description"
    
    def increaseStock(self, amount):
        if amount >= 1:
            if self.__quantityInStock + amount <= 100:
                self.__quantityInStock += amount
            else:
                print("Error: Stock quantity cannot exceed 100.")
        else:
            print("Error: Increased iteam must be greater than or equal to one.")

    def sellStock(self, amount):
        if amount >= 1:
            if amount <= self.__quantityInStock:
                self.__quantityInStock -= amount
                return True
            else:
                print("Error: Insufficient stock to sell.")
        else:
            print(" Error: Sold item must be greater than or equal to one.")
        return False    
    
    def get_VAT(self):
    # Standard VAT rate    
        return 17.5   

    def __str__(self):
        return (f"Stock Category: {self.stockCategory}\n"
               f"Stock Type: {self.get_stockName()}\n" 
               f"Description: {self.get_stockDescription()}\n"
               f"Stock Code: {self.__stockCode}\n" 
               f"Price Without VAT: {self.__priceWithoutVAT}\n"
               f"Price With VAT: {self.get_priceWithVAT():.2f}\n" 
               f"Total Unit in stock: {self.__quantityInStock}\n")
    

# lets run
    
# Create StocKItem object 
item = StockItem("W101", 10, 99.99)

# Print stock information
print("Printing item stock information:")
print(item)

# Increasing stock and Print information
item.increaseStock(10)
print("Printing item stock information:")
print(item)

# sell stock and Print information
item.sellStock(2)
print("Printing item stock information:")
print(item)

# Set new price and Print information
item.set_priceWithoutVAT(100.99)
print("Printing item stock information:")
print(item)

# Increase stock by 0 units (error case)
item.increaseStock(0)
