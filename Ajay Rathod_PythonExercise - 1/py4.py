#Write a Python program to get the volume of a sphere with radius 15.
#Formula - 4/3 πr3


# without function
PI = 3.14 # values of pi
radius = 15 # values of radius

Volume = (4 / 3) * PI * radius * radius * radius # volume of a sphere formula
print("\n The Volume of a Sphere = %.2f" %Volume) # print the volume of a sphere


def fun(radius): # create a def function and inside write a variable for radius
    return (4 / 3) * PI * radius * radius * radius # return values here and volume of a sphere formula

print(fun(3)) # print the volume of a sphere and function calling

x=lambda a: (4 / 3) * 3.14*a*a*a # use of lambda function and write to formula
print(x(3)) # calling function
