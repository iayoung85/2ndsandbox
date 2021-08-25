def wages(hours,pay,status):
    if status=="exempt":
        wages=hours*pay
    elif hours>40:
        wages=40*pay+(hours-40)*1.5*pay
    else:
        wages=hours*pay
    return wages
    