


products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

#group the list
grouped_products = {}

for product in products:
    if product not in grouped_products:
        grouped_products[product] = 1
    else:
        grouped_products[product] +=1    
#print keys if count is 1

print ([k for (k,v) in grouped_products.items() if v==1])