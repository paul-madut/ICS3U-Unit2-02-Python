#!/usr/bin//env python3

# Created by: Paul Madut
# Created on: September 2019
# This is the a program used to calculate area/perimter of a rectangle


import math


def main():
    # This functions calculates area and perimeter
    # Input
    Length = int(input("Enter Length of rectangle (mm):"))
    Width = int(input("Enter Width of rectangle (mm):"))
    # Process
    Area = Length*Width
    Perimeter = 2*(Length + Width)
    # Output
    print("")
    print("Area is {}mm²".format(Area))
    print("Perimeter is {}mm".format(Perimeter))


if __name__ == "__main__":
    main()
