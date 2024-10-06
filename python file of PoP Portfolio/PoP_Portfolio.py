  
# pop protfolio step2(include step1)

# declare class
class StockItem:
    # Class variable
    stock_category = "Car Accessories"

    # constructor to initilize stockItem instance
    def __init__(self, stockCode, quantity, price):

        # Private variables   
        self.__stockCode = stockCode
        self.__quantity = quantity
        self.__price = price

    
    
     # Geters & setters methods for stockcode, quantity and price
    def set_stockCode(self, stockCode):
        self.__stockCode = stockCode

    def get_stockCode(self):
        return self.__stockCode

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_priceWithoutVAT(self, price):
        self.__price = price
        print("\nSet new price", self.__price, "per unit")

    def get_priceWithVAT(self, VAT = 17.5):
         # calculate the price with VAT
         # Declere VAT constant
        return self.__price * (1 + VAT / 100)

    
    def increaseStock(self, amount):
        # The amount is non-negative before increase the quantity in stock
        if amount < 1:
            print("Increasing 0 more units")
            print("The error was: increased Item must be greater than or equal to one")
        elif self.__quantity + amount > 100:
            # Stock exceeds 100
            print("stock exceeds 100 units")
        else:
            self.__quantity += amount
            print("Increasing", amount, "more units")


    def sellStock(self, amount):
        # The amooumt is between 0 and the current quantity before  decrease
        if amount < 1:
            print("The error was: sold item must be greater than or equal to 0")
            return False
        elif amount <= self.__quantity:
            self.__quantity -= amount
            print("Sold", amount, "units")
            return True
        else:
            print("Insufficient Stock")
            return False

    # print information about the stock item
    def __str__(self):
        return (f"Printing item stock information:\n"
                f"Stock Category: {StockItem.stock_category}\n"
                f"Stock Type: {self.getStockName()}\n"
                f"Description: {self.getStockDescription()}\n"
                f"StockCode: {self.__stockCode}\n"
                f"PriceWithoutVAT: {self.__price:.2f}\n"
                f"PriceWithVAT: {self.get_priceWithVAT():.2f}\n"
                f"Total unit in stock: {self.__quantity}\n")

    @staticmethod
    def getStockName():
        return "Unknown Stock Name"

    @staticmethod
    def getStockDescription():
        return "Unknown Stock Description"



# create a subclass for navigation systems 
class NavSys(StockItem):
    def __init__(self, stockCode, quantity, price, brand):
        # Call the constructor of the base class using super()
        super().__init__(stockCode, quantity, price)
         # Add a new attribute specific to navigatiion systen
        self._brand = brand


    # Override the base class mthod to return aspecific stockname for navigation systems
    def getStockName(self):
        return "Navigation system"

    # override the base class method to return a specific description for navigation systems
    def getStockDescription(self):
        return "GeoVision Sat Nav"

    def __str__(self):
        # call superclass (StockItem) to get stock information
        stock_info = super().__str__()
        # Add additional (brand) information for navigation systems
        return stock_info + f"Brand: {self._brand}\n"

# Create StocKItem object item(step1 output)
def stock_item_example():
    item = StockItem("W101", 10, 99.99)
     # Creating a stock with 10 units Unknown item, price 99.99 each, and item code W101
    print("\nCreating a stock with", item.get_quantity(), "units Unknown item, price", item.get_price(), "each, and item code", item.get_stockCode())
   
    # Print stock information
    print(item.__str__())

    # Increasing stock and Print information
    item.increaseStock(10)
    print(item.__str__())

    # sell stock and Print information
    item.sellStock(2)
    print(item.__str__())

    # Set new price and Print information
    item.set_priceWithoutVAT(100.99)
    print(item.__str__())

    # Increase stock by 0 units (error case)
    item.increaseStock(0)

# Create StocKItem object item2 (step2 output)
def nav_sys_example():
    item2 = NavSys("NS101", 10, 99.99, "TomTom")

    # Creating a stock with 10 units Navigation system, price 99.99, item code NS101, brand TomTom 
    print(f"\nCreating a stock with {item2.get_quantity()} navigation system, price {item2.get_price()} item code {item2.get_stockCode()} and brand {item2._brand}")

    print(item2.__str__())


    # Increasing stock and Print information
    item2.increaseStock(10)
    print(item2.__str__())

    # sell stock and Print information
    item2.sellStock(2)
    print(item2.__str__())

    # Set new price and Print information
    item2.set_price(120.00)
    print(item2.__str__())
    
    # Increase stock by 0 units (error case)
    item2.increaseStock(0)

 # Call the stock_item_example function to run operations on a StockItem object
stock_item_example()
 # Call the nav_sys_example function to run operations on a NavSys object
nav_sys_example()



print("@Foyez Ahammed-11/01/2024")