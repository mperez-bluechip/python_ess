#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    n = 42
    s = 'This is a string!'
    print(s)

    s = 'This is a\nstring!'
    print(s)

    #raw string
    s = r'This is a\nstring!'
    print(s)

    s = 'This is a {} string!'.format(n)
    print(s)

    s = '''\
    this is a string
    line after line
    of text and more
    text.
    '''
    print(s)

if __name__ == "__main__": main()
