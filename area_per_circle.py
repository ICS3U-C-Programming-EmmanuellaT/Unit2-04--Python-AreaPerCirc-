#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 29th Sep, 2026
# This program asks the radius of a circle in cm
# it then calculates the Area and Circumference of the
# circle and displays the results to the user with proper units.
import math


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (cm): "))

    # calculate the area and circumference of a circle
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    # display the area and circumference to the user with proper units
    print("The area is: {:.2f}cm²".format(area))
    print("The circumference is: {:.2f}cm".format(circumference))


if __name__ == "__main__":
    main()
