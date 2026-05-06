# creating a tuple
# arrray of tuples
orders=[
    (1001, "Alice", "Laptop", 75000),
    (1002, "Bob", "Phone", 25000),
    (1003, "Alice", "Mouse", 500),
    (1004, "Charlie", "Laptop", 75000),
    (1005, "Bob", "Keyboard", 1500),
    (1006, "Alice", "Keyboard", 1500),
    (1007, "Charlie", "Phone", 25000),
    (1008, "Bob", "Mouse", 500),
    (1009, "David", "Laptop", 75000),
    (1010, "Charlie", "Mouse", 500),
]
# finding the name who have ordered more than once
name_count={}

for order in orders:
    name=order[1]
    
    if name in name_count:
        name_count[name]+=1
    else:
        name_count[name]=1

for name in name_count:
    if(name_count[name]>1):
        print(name)
    

# finding who has spend more

spending={}


for order in orders:
    money=order[3]
    name=order[1]
    
    if name in spending:
        spending[name]+=money
    else:
        spending[name]=money
        
top=max(spending.values())

print(top)

# products bought by every customer
customer={}

for order in orders:
    name=order[1]
    product=order[2]
    
    if name in customer:
        customer[name].append(product)
    else:
        customer[name]=[product]
        
        
print(customer)
  
        


        
           

        
    
    
    
    
