import isaacmodule

baseteninteger=input('enter a base-ten integer')
output=isaacmodule.base_ten_to_hex(baseteninteger)
print(output)

number = ''.join(map(str, output))
print(number)