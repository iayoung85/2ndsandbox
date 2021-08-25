#given a list of integers separated by spaces, counts number of even integers in list
def count_even_numbers(s):
    listints=s.split()
    count=0
    for n in listints:
        try:
            if int(n)%2==0:
                count+=1
        except: 
            print('invalid string. one or more values may not have been an integer')
            print('skipping the invalid value')
    return count
