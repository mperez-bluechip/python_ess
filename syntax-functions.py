#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    #func()

# def func():
#     for i in range(10):
#         print(i)

#     func(1)
#     func(3)
#     func(5)
#
# def func(a):
#     for i in range(a, 10):
#         print(i)

    func(1)
    func()
    func(5)

def func(a=7):
    for i in range(a, 10):
        print(i)


if __name__ == "__main__": main()
