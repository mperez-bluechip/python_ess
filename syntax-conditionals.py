#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # a, b = 2, 1
    # if a < b:
    #     print("a is less than b")
    # elif a > b:
    #     print('a is greater than b')
    # else:
    #     print('a is equal to b')

    a, b = 1, 1
    s = 'less than' if a < b else 'not less than'
    print(s)



if __name__ == "__main__": main()
