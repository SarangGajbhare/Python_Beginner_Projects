import math

print("=====================")
print("Area Calculator")
print("=====================")
print()
while True:
    print("Choose a shape")
    print()
    print("1) Square")
    print("2) Rectangle")
    print("3) Triangle")
    print("4) Circle")

    select = int(input("Enter a shape number: "))

    if(select == 1):
        side = float(input("Enter a side: "))
        area = math.pow(side, 2)
        print(f"Area of Square is: {area:.2f}")
        print()

    elif(select == 2):
        length = float(input("Enter a Lenght of Rectangle: "))
        width  = float(input("Enter a Width of Rectangle: "))
        area  = length  * width
        print(f"Area of Rectangle is {area:2f}")
        print()

    elif(select == 3):
        height = float(input("Enter a Height if Triangle: "))
        base = float(input("Enter Base of Triangle: "))
        area = (height * base) / 2
        print(f"Area of Triangle is {area:.2f}")
        print()

    elif(select == 4):
        radius = float(input("Enter a Radius of Circle: "))
        area = math.pi * (radius * radius)
        print(f"Area of Circle is {area:.2f}")
        print()
    else:
        print("Invalid option you choosed")