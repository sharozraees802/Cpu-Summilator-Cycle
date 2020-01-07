from IPython.display import Markdown,display

def printmd(string):
    display(Markdown(string))
printmd("<span style='color:green; font-size:22px'><b>helloword</b></span>")


number = int(input('Enter decimal number: '))
number1 = int(input("Enter a decimal number2: "))
address = int(input("Enter a address where you want to insert the value: "))
print()

print("For Adiition Enter: + ")
print("For subtraction Enter: - ")
print("For Multiplication Enter: * ")
print("For Division Enter: / ")
print()
operator = str(input("Enter a operator: "))
print("FETCH-Before Decode")
Arr = [number, number1, operator, address]
print(Arr)
print()


# first number in decode or binary /  decimal to binary
temp = ''
while True:
    if number < 0:
        print("the value is negative binary is not in neagative number:")
        number = -(number)
    if number > 0:

        temp += str(number % 2)
        number = number // 2
    else:
        break
number_decimal = ''
for i in range(len(temp)-1, -1, -1):
    number_decimal += temp[i]
# second number decode or binary   /  decimal to binary
temp1 = ''
while True:
    if number1 < 0:
        print("the value is negative binary is not in neagative number:")
        number1 = -(number1)
    if number1 > 0:
        temp1 += str(number1 % 2)
        number1 = number1 // 2
    else:
        break
number1_decimal = ''
for i in range(len(temp1)-1, -1, -1):
    number1_decimal += temp1[i]
# Addres decode or binary  /  decimal to binary
temp3 = ''
while True:
    if address < 0:
        print("the value is negative so negative  address  is not reconize")
        address = -(address)
    if address > 0:
        temp3 +=str(address % 2)
        address = address // 2
    else:
        break
address_decimal = ''
for i in range(len(temp3)-1, -1, -1):
    address_decimal += temp3[i]

# operator decode or binary  /  decimal to binary
operator1 = ""
if Arr[2] == "+":
    operator1 = "0000"
elif Arr[2] == "-":
    operator1 = "0001"
elif Arr[2] == "*":
    operator1 = "0010"
elif Arr[2] == "/":
    operator1 = "0011"

print("Decode")

print(Arr)
print()

# convert binary to decimal binary_number
power = 0
while number_decimal != 0:
    number_decimal = int(number_decimal)
    digit = int(number_decimal % 10)
    number = number + (digit*2**power)
    power += 1
    number_decimal = int(number_decimal/10)

# convert binary to decimal binary_number1
power = 0
while(number1_decimal != 0):
   number1_decimal = int(number1_decimal)
   digit1 = int(number1_decimal%10)
   number1 = number1 + (digit1*2**power)
   power += 1
   number1_decimal = int(number1_decimal/10)

# convert binary to decimal binary_Address
power = 0
while address_decimal !=0:
    address_decimal = int(address_decimal )
    digit2 = int(address_decimal % 10)
    address = address + (digit2*2**power)
    power +=1
    address_decimal = int(address_decimal/10)



# calculation perfome
if operator == "+":
    result = number + number1
    if result < 0:
        print("the value is negative binary is not in neagative number:")
        result = -(result)
    address = result
elif operator == "-":
    result = number - number1
    if result < 0:
        print("the value is negative binary is not in neagative number:")
        result = -(result)
    address = result
elif operator == "*":
    result = number * number1
    if result < 0:
        print("the value is negative binary is not in neagative number:")
        result = -(result)
    address = result
elif operator == "/":
    result = int(number / number1)
    if result < 0:
        print("the value is negative binary is not in neagative number:")
        result = -(result)
    if result == 0 or result == 1:
        result += 1
        address = result
    else:    # print(result)
        address = result

    # if result <
    address = result

print("calculation  perform:")
# again convert deimal to bianry
temp = ''
while True:
    if number > 0:
        temp += str(number % 2)
        number = number // 2
    else:
        break
number_decimal = ''
for i in range(len(temp)-1, -1, -1):
    number_decimal += temp[i]
# second number decode
temp1 = ''
while True:
    if number1 > 0:
        temp1 += str(number1 % 2)
        number1 = number1 // 2
    else:
        break
number1_decimal = ''
for i in range(len(temp1)-1, -1, -1):
    number1_decimal += temp1[i]
# Addres decode
temp3 = ''
while True:
    if address > 0:
        temp3 +=str(address % 2)
        address = address // 2
    else:
        break
address_decimal = ''
for i in range(len(temp3)-1, -1, -1):
    address_decimal += temp3[i]

Arr=[number_decimal, number1_decimal, operator1, address_decimal]
print(Arr)
print()

print("Excute and Encode:")
# convert binary to decimal binary_number
power = 0
while number_decimal != 0:
    number_decimal = int(number_decimal)
    digit = int(number_decimal % 10)
    number = number + (digit*2**power)
    power += 1
    number_decimal = int(number_decimal/10)

# convert binary to decimal binary_number1
power = 0
while(number1_decimal != 0):
   number1_decimal = int(number1_decimal)
   digit1 = int(number1_decimal%10)
   number1 = number1 + (digit1*2**power)
   power += 1
   number1_decimal = int(number1_decimal/10)

# convert binary to decimal binary_Address
power = 0
while address_decimal !=0:
    address_decimal = int(address_decimal )
    digit2 = int(address_decimal % 10)
    address = address + (digit2*2**power)
    power +=1
    address_decimal = int(address_decimal/10)

Arr=[number, number1 , operator, address]
print(Arr)
