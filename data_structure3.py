# count for file lines
def count(Filename):
    file = open(Filename)
    count = 0
    count1 =0
    for i in file:

        count +=1
        # print(count)
    # for j in range(0,count,count):
        # count1 += 1
        # print(count1)

    return count





FILENAME  = 'DATA_OPERATION1.txt'

File = open(FILENAME,'r')
Count = 0
for i in range(0,count(FILENAME)):
    Arr = []
    lines = File.readlines()
    for line in lines:
        numbers = line.split(',')
        Count +=1
        for j in range(1,2):
            f = str(File.readline())
            numbers.append(f)
            number_decimal = numbers[0]
            number1_decimal = numbers[1]
            operator_decimal = numbers[2]
            address_decimal = numbers[3]
            power = 0
            number = 0
            # binary into decimal
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

            # converting operators into decimal +-*/
            operator = ""
            if operator_decimal == "0000":
                operator = "+"
            elif operator_decimal == "0001":
                operator = "-"
            elif operator_decimal == "0010":
                operator = "*"
            elif operator_decimal == "0011":
                operator = "/"

            print("FETCH-Before Decode")
            Arr=[number, number1, operator, address]
            print(Arr)

            # first number converted into binary
            temp = ''
            while True:
                if number < 0:
                    print("we got negative number first we will convert it into positive then in binary :")
                    number = -(number)
                if number > 0:

                    temp += str(number % 2)
                    number = number // 2
                else:
                    break


            number_decimal = ''
            for i in range(len(temp) - 1, -1, -1):
                number_decimal += temp[i]


            # second number converted into binary
            temp1 = ''
            while True:
                if number1 < 0:
                    print("we got negative number:")
                    number1 = -(number1)
                if number1 > 0:
                    temp1 += str(number1 % 2)
                    number1 = number1 // 2
                else:
                    break
            number1_decimal = ''
            for i in range(len(temp1) - 1, -1, -1):
                number1_decimal += temp1[i]


            #address converting into binary
            temp3 = ''
            while True:
                if address < 0:
                    print("we got negative address")
                    address = -(address)
                if address > 0:
                    temp3 += str(address % 2)
                    address = address // 2
                else:
                    break
            address_decimal = ''
            for i in range(len(temp3) - 1, -1, -1):
                address_decimal += temp3[i]

                # converting operations into binary
            operator_decimal = ""
            if Arr[2] == "+":
                operator_decimal = "0000"
            elif Arr[2] == "-":
                operator_decimal = "0001"
            elif Arr[2] == "*":
                operator_decimal = "0010"
            elif Arr[2] == "/":
                operator_decimal = "0011"


           #decoding
            print("Decode")
            Arr = [number_decimal, number1_decimal, operator_decimal, address_decimal]
            print(Arr)



            # calculation
            print("Calculation  Perform after Decode:")

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




            #converting binary operations into decimal then again in binary
            if operator == "+":
                result = number + number1
                if result < 0:
                    print("we got negative result:")
                    result = -(result)
                address = result
            elif operator == "-":
                result = number - number1
                if result < 0:
                    print("we got negative result:")
                    result = -(result)
                address = result
            elif operator == "*":
                result = number * number1
                if result < 0:
                    print("we got negative result:")
                    result = -(result)
                address = result
            elif operator == "/":
                result = int(number / number1)
                if result < 0:
                    print("we got negative result:")
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
            # Address decode
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
