#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    num = 42
    print(num)

    num = 42
    print(type(num), num)

    num = 42.0
    print(type(num), num)

    num = 42 / 9
    print(type(num), num)

    num = 42 // 9
    print(type(num), num)

    num = round(42 / 9)
    print(type(num), num)

    num = round(42 / 9, 2)
    print(type(num), num)

    num = 42 % 9
    print(type(num), num)

    num = int(42.9)
    print(type(num), num)

    num = float(42)
    print(type(num), num)

if __name__ == "__main__": main()
