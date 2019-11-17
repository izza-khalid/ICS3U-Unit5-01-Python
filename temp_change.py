#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: November 2019
# This program uses user defined functions


def fahren():
    # convert celsius to fahrenheit

    # input
    print("We are converting temperature from celsius to fahrenhei! ")
    print("")
    celsius = int(input("Enter the temperature in °C: "))

    # process
    temp_fahren = ((9/5 * celsius) + 32)

    # output
    print("The temperature is {0}°F".format(temp_fahren))


def main():
    # this function just calls other functions

    # call functions
    fahren()


if __name__ == "__main__":
    main()
