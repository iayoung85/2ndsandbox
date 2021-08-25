#returns calculated pay assuming overtime hours are 1.5x normal pay
def computepay(hours_worked,pay_rate):
    if(float(hours_worked)<=40):
        return float(hours_worked)*float(pay_rate)
    else:
        return 40*float(pay_rate)+(1.5*(float(hours_worked)-40)*float(pay_rate))

hours=input('Hours of work done this week: ')
pay=input('How much do you get paid per hour in USD currency:  ')
print('# of hours entered: '+hours)
print('pay per hour: $'+pay)

total_pay=computepay(hours,pay)
if float(total_pay)>=500:
    print('you rich!')
else:
    print('you broke!')

print(type(total_pay))
print('$'+str(int(total_pay)))