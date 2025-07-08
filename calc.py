# calculator

import math

# functions
print("1. add \n2. subtract \n3. multiply \n4. divide \n5. squareRoot \n6. percentage \n7. discount \n8 .exponent")

#reference
#add = x + y
#subtract = x - y
#multiply = x * y
#divide = x/y
#squareRoot = x^(1/2)
#percentage = (x/y)*100
#discount = x - x*(y/100)
#exponent = x^y

#inputCode
function = int(input("enter the function you'd like to use: "))
print(function)
if function == 1:
    x = float(input("firstNumber: "))
    y = float(input("secondNumber: "))
    print(x + y)
elif function == 2:
    x = float(input("firstNumber: "))
    y = float(input("secondNumber: "))
    print( x - y)
elif function == 3:
    x = float(input("firstNumber: "))
    y = float(input("secondNumber: "))
    print( x * y)
elif function == 4:
    x = float(input("firstNumber: "))
    y = float(input("secondNumber: "))
    print(x/y)
elif function == 5:
    x = int(input("Number: "))
    print(math.sqrt(x))
elif function == 6:
    x = float(int(input("Value: ")))
    y = float(int(input("Total: ")))
    print((x/y)*100)
elif function == 7:
    x = float(input("Value: "))
    y = float(input("Discount: "))
    print(x - x*(y/100))
elif function == 8:
    x = float(input("Number: "))
    y = float(input("Power: "))
    print(math.pow(x.y))
else:
    print("error")

    
              
