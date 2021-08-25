#LED lights are $5 each and $46 per box of 10. 
#shipping is $4 per box whether or not the box is full. 
#determine total cost of an order of LED lights
def LEDlightbulbs_order_cost(how_many):
    numbox=how_many//10
    numextra=how_many-10*numbox
    shipping=4*numbox
    if numextra!=0:
        shipping+=4
    totalcost=shipping+5*numextra+46*numbox
    return totalcost
print(LEDlightbulbs_order_cost(32))
