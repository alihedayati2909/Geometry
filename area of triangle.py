import math
print("Welcome to this code:) in this code you can calculate the area of any triangle and you can find the height corresponding to the longest side of the triangle. Good luck! ")
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))
if (a + b) > c and (a + c) > b and (b + c) > a:
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))

    if a >= b and a >= c:
        h = (2*s)/a
    elif c >= b and c >= a:
        h = (2*s)/c
    elif b >= a and b >= c:
        h = (2*s)/b
    else:
        print("Error")

    print(f"the area is equal to {s:.2f}, and the height corresponding to the longest side of the triangle is equal to {h:.2f} ")
else:
    print("your shape is not a triangle!")
