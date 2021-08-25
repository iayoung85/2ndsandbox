x=input('What is your final points?')
def curve(x):
    try:
        if(float(x)<0):
            print('You must enter a value greater than 0')
        elif(float(x)<=62.4):
            print('Your points: 25.0 your letter grade: F, sorry you fail')
        elif(float(x)<=72.4):
            print('your points: 65.0 Your letter grade: D')
        elif(float(x)<=82.4):
            print('Your points: 75 Your letter grade: C')
        elif(float(x)<=92.4):
            print('Your points: 85.0 Your letter grade: B')
        elif(float(x)<=100):
            print('Your points: 95.0 Your letter grade: A, good job!')
        else:
            print('You cannot earn more than 100 points on the final')
    except:
        print('please enter numeric values')
calculation=curve(x)
print(calculation)