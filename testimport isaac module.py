import isaacmodule

hours=input('Hours of work done this week: ')
pay=input('How much do you get paid per hour in USD currency:  ')
print('# of hours entered: '+hours)
print('pay per hour: $'+pay)

total_pay=isaacmodule.computepay(hours,pay)
if float(total_pay)>=500:
    print('you rich!')
else:
    print('you broke!')

print(type(total_pay))
print('$'+str(int(total_pay)))
