#figure 3 program
def postage(weight):
    import math
    costfig3=49
    if weight>1:
        costfig3=costfig3+22*math.ceil(weight-1)
    if weight>3.5:
        costfig3 +=49
    return costfig3/100