#figure 2 program
def postage(weight):
    import math
    if weight<=1:
        costfig2=49
    elif weight>1:
        costfig2=49+22*math.ceil(weight-1)
    elif weight>3.5:
        costfig2=98+22*math.ceil(weight-1)
    else:
        costfig2=49+math.ceil(weight-1)*22
    return costfig2/100