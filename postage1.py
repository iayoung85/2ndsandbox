# figure 1 function
def postage(weight):
    import math
    if weight<=1:
        cost=49
    elif weight<=3.5:
        cost=49+math.ceil(weight-1)*22
    else:
        cost=98+22*math.ceil(weight-1)
    return cost/100