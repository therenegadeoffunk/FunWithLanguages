#!/usr/bin/env python

# Some good ol' mergesort.

def mergesort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    else:
        middle = int(len(unsorted)/2)
        a = mergesort(unsorted[:middle])
        b = mergesort(unsorted[middle:])
        i = 0
        j = 0
        final = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                final.append(a[i])
                i += 1
            else:
                final.append(b[j])
                j += 1
        final += a[i:]
        final += b[j:]
        return final

def test_sort():
    testlist = [9,5,3,8,2,11,6,4,1,2]
    sorted = mergesort(testlist)
    print sorted

if __name__ == "__main__":
    test_sort()
