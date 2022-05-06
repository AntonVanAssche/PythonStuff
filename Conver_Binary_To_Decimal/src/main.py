#!/usr/bin/env python3

try:
    menu = int(input("Options: \n\t1) Decimal to binary \n\t2) Binary to decimal\nSelection: "))

    if menu == 1:
        dec = int(input("Input your decimal number:\nDecimal: "))
        print("Binary: {}".format(bin(dec)[2:]))
    elif menu == 2:
        bin = input("Input your binary number:\nBinary: ")
        print("Decimal: {}".format(int(bin, 2)))
    else:
        raise ValueError
except ValueError:
    print ("Please choose a valid option")
