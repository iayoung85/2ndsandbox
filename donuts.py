print("Welcome to Isaac's Donut Shop!")
print("Donuts cost $0.75 each or $8.00 for each dozen which saves you 1 dollar!")
donuts=input("How many donuts would you like? ")
flavor=input("Would you like chocolate or vanilla donuts? ")   
    while flavor!='chocolate' and flavor!='vanilla':
        print("I'm sorry but we only have chocolate and vanilla donuts at this time")
        flavor=input("Would you like chocolate or vanilla donuts? ")
    else:
        dozen=int(donuts)/12
        remain=int(donuts)%12
        price=int(dozen)*8+remain*.75
        print("Thanks for your order of " + donuts, flavor,"donuts!")
        print("Your total bill comes to $"+str(price))