import math

print("============")
print("Calculator")
print("============")
print()

print("1) Addition(+)")
print("2) Subsraction(-)")
print("3) Multiplication(*)")
print("4) Division(/)")
print("5) Power")
print("6) Square Root")
print("7) Module(%)") 
print()

while True:
    try:
        select = int(input("Enter a Opeartor No.: "))
        print()
        if select == 1 or select == 2 or select == 3 or select == 4 or select == 5 or select == 7:
            first_num = int(input("Enter a first Number: "))
            second_num = int(input("Enter a second Number or Powers : "))
        else:
            first_num = int(input("Enter a first Number: "))
            
        if select == 1:
            result = first_num + second_num
            print(f"Addition of both number is :{result}\n")
            break 
        elif select == 2:
            result = first_num - second_num
            print(f"Substraction of both number is :{result}\n")
            break
        elif select == 3:
            result = first_num * second_num
            print(f"Multiplication of both number is :{result}\n")
            break
        elif select == 4:
            result = first_num / second_num
            print(f"Division of both number is :{result:.2f}\n")
            break 
        elif select == 5:
            result = math.pow(first_num, second_num)
            print(f"Power of {first_num} is {result}")
            break
        elif select == 6:
            result = math.sqrt(first_num)
            print(f"Square root of {first_num} is {result:.2f}")
            break
        elif select == 7:
            result = first_num % second_num
            print(result)
                           
    except ZeroDivisionError:
        print("Error, Integer cannot divided by zero")
        
    except ValueError:
        print("Enter a only integer")

        


