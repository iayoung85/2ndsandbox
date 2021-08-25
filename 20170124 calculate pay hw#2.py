b=input('Hours of work done this week: ')
d=input('How much do you get paid per hour in USD currency:  ')
print('# of hours entered:   '+b)
print('pay per hour:   $'+d)
try:
    if(float(b)<=40):
        e=float(b)*float(d)
        print('$'+str(e))
        if float(e)>int(500):
            print('you rich!')
        if float(e)<int(500):
            print('you broke!')
    else:
        f=40*float(d)+(1.5*(float(b)-40)*float(d))
        print('$'+str(f))
        if float(f)>int(500):
            print('you rich!')
        if float(f)<int(500):
            print('you broke!')
except:
    print('please enter numeric values')