import math

print("============")
print("Calculator")
print("============")
print()

print("1) Addition(+)")
print("2) Subsraction(-)")
print("3) Multiplication(*)")
print("4) Division(/)")
print()

while True:
    try:
        select = int(input("Enter a Opeartor No.: "))
        print()
        if select == 1:
            first_num = float(input("Enter a first number: "))
            second_num = float(input("Enter a second number:  "))
            result = first_num + second_num
            print(f"Addition of both number is :{result}\n")
            
        elif select == 2:
            first_num = float(input("Enter a first number: "))
            second_num = float(input("Enter a second number:  "))
            result = first_num - second_num
            print(f"Substraction of both number is :{result}\n")

        elif select == 3:
            first_num = float(input("Enter a first number: "))
            second_num = float(input("Enter a second number:  "))
            result = first_num * second_num
            print(f"Multiplication of both number is :{result}\n")

        elif select == 4:
            first_num = float(input("Enter a first number: "))
            second_num = float(input("Enter a second number:  "))
            result = first_num / second_num
            print(f"Division of both number is :{result:.2f}\n")
        
    except ZeroDivisionError:
        print("Error, Integer cannot divided by zero")
        
    except ValueError:
        print("Enter a only integer")

        


