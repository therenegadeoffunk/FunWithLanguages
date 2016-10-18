#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print "gonna need an argument there, sport"
    exit(0)

filepath = sys.argv[1]
stringlist = open(filepath, 'r').readlines()
intlist = map(int, stringlist)

def partition(datlist, start, finish):
    pivotvalue = datlist[start]
    left = start + 1
    right = finish
    done = False
    while not done:

        while left <= right and datlist[left] <= pivotvalue:
            left = left + 1
        while datlist[right] >= pivotvalue and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            k = datlist[left]
            datlist[left] = datlist[right]
            datlist[right] = k
    k = datlist[start]
    datlist[start] = datlist[right]
    datlist[right] = k
    return right
                
def quick_sort(datlist, start, finish):
    if start < finish:
        part = partition(datlist, start, finish)
        quick_sort(datlist, start, part-1)
        quick_sort(datlist, part+1, finish)

if __name__ == "__main__":
    finish = len(intlist) - 1
    quick_sort(intlist, 0, finish)
    print intlist
