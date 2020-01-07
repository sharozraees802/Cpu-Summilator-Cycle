# file ki line ko countikar rha  h
def count(Filename):
    file = open(Filename)
    count = 0
    count1 =0
    for i in file:
        count +=1
    for j in range(0,count,4):
        # uper wala count agr 4 ho ga yah loop one time chaly ga
        count1 += 1
    return count1
    # file.close()



# file ka naam h yah
Filename = 'DATA_OPERATION.txt'
# file open kari h aur end me close karna lazim h
File = open(Filename,'r')

# count file ka method uper h
Count = 0
for i in range(0,count(Filename)):
    Arr = []
    Count +=1
    for j in range(1,5):
        f = int(File.readline())

        Arr.append(f)
    number_decimal = Arr[0]
    number1_decimal = Arr[1]
    operator_decimal = Arr[2]
    address_decimal = Arr[3]
    power = 0
    number = 0
    # yaha sari binary arhi han phr me unko convert kar rha hn deimal me
    while number_decimal != 0:
        number_decimal = int(number_decimal)
        digit = int(number_decimal % 10)
        number = number + (digit * 2 ** power)
        power += 1
        number_decimal = int(number_decimal / 10)

    power = 0
    number1 = 0
    while (number1_decimal != 0):
        number1_decimal = int(number1_decimal)
        digit1 = int(number1_decimal % 10)
        number1 = number1 + (digit1 * 2 ** power)
        power += 1
        number1_decimal = int(number1_decimal / 10)

    power = 0
    address = 0
    while address_decimal != 0:
        address_decimal = int(address_decimal)
        digit2 = int(address_decimal % 10)
        address = address + (digit2 * 2 ** power)
        power += 1
        address_decimal = int(address_decimal / 10)
    # yaha operation convert ho rhy han
    operator = ""
    if operator_decimal == 0:
        operator = "+"
    elif operator_decimal == 1:
         operator = "-"
    elif operator_decimal == 10:
        operator = "*"
    elif operator_decimal == 11:
        operator = "/"
    # Arr = [number, number1, operator_decimal[2] , address]
    print("FETCH-Before Decode")
    Arr = [number, number1, operator,  address]
    print(Arr)

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
    for i in range(len(temp) - 1, -1, -1):
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
    for i in range(len(temp1) - 1, -1, -1):
        number1_decimal += temp1[i]
    # Addres decode or binary  /  decimal to binary
    temp3 = ''
    while True:
        if address < 0:
            print("the value is negative so negative  address  is not reconize")
            address = -(address)
        if address > 0:
            temp3 += str(address % 2)
            address = address // 2
        else:
            break
    address_decimal = ''
    for i in range(len(temp3) - 1, -1, -1):
        address_decimal += temp3[i]

    # again operation convert ho rha han decimal to binary
    operator_decimal = ""
    if Arr[2] == "+":
        operator_decimal = "0000"
    elif Arr[2] == "-":
        operator_decimal = "0001"
    elif Arr[2] == "*":
        operator_decimal = "0010"
    elif Arr[2] == "/":
        operator_decimal = "0011"
    print("Decode")
    Arr = [number_decimal, number1_decimal, operator_decimal, address_decimal]
    print(Arr)

# calculation
    print("calculation  perform:")
    power = 0
    number = 0
    while number_decimal != 0:
        number_decimal = int(number_decimal)
        digit = int(number_decimal % 10)
        number = number + (digit * 2 ** power)
        power += 1
        number_decimal = int(number_decimal / 10)

    power = 0
    number1 = 0
    while (number1_decimal != 0):
        number1_decimal = int(number1_decimal)
        digit1 = int(number1_decimal % 10)
        number1 = number1 + (digit1 * 2 ** power)
        power += 1
        number1_decimal = int(number1_decimal / 10)

    power = 0
    address = 0
    while address_decimal != 0:
        address_decimal = int(address_decimal)
        digit2 = int(address_decimal % 10)
        address = address + (digit2 * 2 ** power)
        power += 1
        address_decimal = int(address_decimal / 10)
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
        else:  # print(result)
            address = result



    # print(address)
    temp = ''
    while True:
        if number > 0:
            temp += str(number % 2)
            number = number // 2
        else:
            break
    number_decimal = ''
    for i in range(len(temp) - 1, -1, -1):
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
    for i in range(len(temp1) - 1, -1, -1):
        number1_decimal += temp1[i]
    # Addres decode
    temp3 = ''
    while True:
        if address > 0:
            temp3 += str(address % 2)
            address = address // 2
        else:
            break
    address_decimal = ''
    for i in range(len(temp3) - 1, -1, -1):
        address_decimal += temp3[i]

    Arr = [number_decimal, number1_decimal, operator_decimal, address_decimal]
    print(Arr)

    print("Excute and Encode:")
    # convert binary to decimal binary_number
    power = 0
    while number_decimal != 0:
        number_decimal = int(number_decimal)
        digit = int(number_decimal % 10)
        number = number + (digit * 2 ** power)
        power += 1
        number_decimal = int(number_decimal / 10)

    # convert binary to decimal binary_number1
    power = 0
    while (number1_decimal != 0):
        number1_decimal = int(number1_decimal)
        digit1 = int(number1_decimal % 10)
        number1 = number1 + (digit1 * 2 ** power)
        power += 1
        number1_decimal = int(number1_decimal / 10)

    # convert binary to decimal binary_Address
    power = 0
    while address_decimal != 0:
        address_decimal = int(address_decimal)
        digit2 = int(address_decimal % 10)
        address = address + (digit2 * 2 ** power)
        power += 1
        address_decimal = int(address_decimal / 10)

    Arr = [number, number1, operator, address]
    print(Arr)
    print()
    print("------------------------" + str(Count) + "----------------------")

File.close()




# file = open('DATA_OPERATION1.txt','r')
# lines = file.readlines()
# for line in lines:
#     numbers = line.split(',')
#     print(numbers)