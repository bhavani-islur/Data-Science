class harley:
    def __init__(self,manu,cheapest_price):
        self.manufacturer=manu
        self.cheapestprice=cheapest_price
        
    def info(self,waiting_period):
        return f"{self.cheapestprice} is for the {self.manufacturer} for waiting {waiting_period}"
    
class bmw:
    def __init__(self,manu,cheapest_price):
        self.manufacturer=manu
        self.cheapestprice=cheapest_price
        
    def info(self):
        return f"{self.cheapestprice} is for the {self.manufacturer} for waiting "
    
har=harley("HD",2500000)
Bm=bmw("BMW",21)

print(har.info(32))

# Method Overriding
class harley:
    def __init__(self,manu,cheapest_price):
        self.manufacturer=manu
        self.cheapestprice=cheapest_price
        
    def info(self,waiting_period):
        return f"{self.cheapestprice} is for the {self.manufacturer} for waiting {waiting_period}"
    
class bmw(harley):
    def __init__(self,manu,cheapest_price):
        self.manufacturer=manu
        self.cheapestprice=cheapest_price
        
    def info(self):
        return f"{self.cheapestprice} is for the {self.manufacturer} for waiting "
    
# har=harley("HD",2500000)
Bm=bmw("BMW",21)

print(Bm.info())

