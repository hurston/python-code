#To call this script from the commandline, save it as areacalculator.py and call this on the terminal:
#python AreaCalculator.py

"""This program will calculate the area of shapes specified
by the user"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Your Shape Calculator is Starting Up"

print str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute)
sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle:")
option = option.upper()
if option == "C":
    radius = float(raw_input("Enter the circle's radius:"))
    area = pi * (radius **2)
    print "The pie is baking..."
    sleep(1)
    print str(round(area,2)) + "\n" + hint
elif option == "T":
    base = float(raw_input("Enter the triangle's base:"))
    height = float(raw_input("Enter the triangle's height:"))
    area = 0.5 * base * height
    print "Uni Bi Tri..."
    sleep(1)
    print str(round(area,2)) + "\n" + hint
else:
    print "You entered garbage, the program will exit"