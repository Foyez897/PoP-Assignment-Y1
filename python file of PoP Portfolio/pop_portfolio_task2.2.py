class StockItem:
    # constructor to initilize stockItem instance
    def __init__(self, stockName, stockDescription, stockCode, Price, quantityInStock):
        self.stockName = stockName
        self.stockDescription = stockDescription
        self.stockCode = stockCode
        self.price = Price
        self.quantityInStock = quantityInStock

     # Setter and Getter methods for stockName
    def getStockName(self):
        return self.stockName
    
    
    def getStockDescription(self):
        return self.stockDescription
    
    # Setter and Getter methods for Quantity in Stock
    def increaseQuantityInStock(self, amount):
        # The amount is non-negative before increase the quantity in stock
        if amount >= 1:
            self.quantityInStock += amount
            print(f"Increasing {amount} more units")
            self.printStockInfo()
        else:
            print("The error was: Increased item must be greater then or equal to One")
        
    def decreaseQuantity(self, amount):
            # The amooumt is between 0 and the current quantity before  decrease
            if 0 <= amount <=self.quantityInStock:
                self.quantityInStock -= amount 
                print(f"Sold {amount} units")
                self.printStockInfo()
            else:
                print("The error was: Decreased item must be between 0 and the current quantity")

    def setPrice(self, newPrice):
            # The price is non-negetive before update
            if newPrice >= 0:
                self.price = newPrice
                print(f"Set new price {newPrice} per unit")
                self.printStockInfo()
            else:
                print(" The error was: Price must be greater than or equal to 0")
        
    def printStockInfo(self):
            # Display information about the stock item
            print("Printing item stock information:")
            print(f"Stock Category: {self.getStockCategory()}")
            print(f"Stock Type: {self.getStockName()}")
            print(f"Description: {self.getStockDescription()}")
            print(f"StockCode: {self.stockCode}")
            print(f"PriceWithoutVAT: {self.price:.2f}")
            print(f"PriceWithVAT: {self.calculatePriceWithVAT():.2f}")
            print(f"Total unit in stock: {self.quantityInStock}")
    def calculatePriceWithVAT(self):
            # calculate the price with VAT
            VAT_rate = 0.175
            return self.price* (1 +VAT_rate)
    
    def getStockCategory(self):
        return "Car accessories"
    

        
# Define a subclass for navigationsystems 
class NavSys(StockItem):
    def __init__(self, stockName, stockDescription, stockCode, price, quantityInStock, brand):
        # Call the constructor of the base class using super()
        super().__init__(stockName, stockDescription, stockCode, price, quantityInStock)
        # Add a new attribute specific to navigatiion systen
        self.brand = brand

    def getStockName(self):
        #Override the base class mthod to return aspecific stockname for navigation systems
        return "Navigation system"
    
    def getStockDescription(self):
        # override the base class method to return a specific description for navigation systems
        return "GeoVision Sat Nav"
    
    def getStockCategory(self):
            return super().getStockCategory()
    
    def printStockInfo(self):
        # Call the base class's printStockInfo method
        super().printStockInfo()
        # Add information about the brand
        print(f"Brand: {self.brand}\n")
    

# testing code
# Create an intance of the NavSys class
nav_sys_item = NavSys("Navgation sytem", "Navigation system" , "NS101", 99.99, 10, "TomTom")
# Print informaton about the navigation sysem
nav_sys_item.printStockInfo()

#perfrom operation on the navigation system
nav_sys_item.increaseQuantityInStock(10)
nav_sys_item.decreaseQuantity(2)
nav_sys_item.setPrice(100.99)
nav_sys_item.increaseQuantityInStock(0)