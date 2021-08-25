b=int(input('hours of work done this week'))
d=int(input('how much do you get paid per hour in USD currency'))
e=b*d
print('$'+str(e))
if float(e)>int(500):
    print('you rich mofo!')
if float(e)<int(500):
    print('you broke mofo!')