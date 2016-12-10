#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    x = (1, 2, 3)
    print(x)

    x = (1, 2, 3)
    print(type(x), x)

    x = [1, 2, 3]
    print(type(x), x)

    x = [1, 2, 3]
    x.append(5)
    print(type(x), x)

    x = [1, 2, 3]
    x.append(5)
    x.insert(0, 7)
    print(type(x), x)

    #mutable
    x = [1, 2, 3]
    x.append(5)
    x.insert(2, 7)
    print(type(x), x)

    #immutable x = (1, 2, 3) causes append error
    # x = (1, 2, 3)
    # x.append(5)
    # x.insert(2, 7)
    # print(type(x), x)

    x = 'string'
    print(type(x), x)
    print(type(x), x[2])
    print(type(x), x[2:4])

    x = (1, 2, 3, 4, 5)
    for i in x:
        print(i)

    x = 'string'
    for i in x:
        print(i)

if __name__ == "__main__": main()
