print("Twinkle, twinkle, little star, how i wonder what you are! up above he world so high, like a diamond in the sky. twinklw, twinkle, little star, how i wonder what you are")


print(3**4)

import sys
print("python version")
print(sys.version)
print("python version_info")
print(sys.version_info)

from datetime import datetime
now= datetime.now()
dt_string= now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time=", dt_string)

x= "Batman"
y= "Superman"
z= "Ironman"
collab= x + " "+ y +" " + z
print(collab)

from math import pi
r= float(input("input the radius of the circle: "))
print("the area of the circle with radius " + str(r) + " is: "+ str(pi * r**2))