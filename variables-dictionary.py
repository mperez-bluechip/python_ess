#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
    print(d)

    #un-ordered output
    d = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
    for k in d:
        print(k, d[k])

    #ordered alphabetically by keys
    d = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
    for k in sorted(d.keys()):
        print(k, d[k])

    #keyword objects
    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    #add seven inside dictionary
    d['seven'] = 7
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()
