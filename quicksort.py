# -*- coding:utf-8 -*-


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    return quick_sort([le for le in arr[1:] if le <= arr[0]]) + arr[0:1] + quick_sort(
        [gt for gt in arr[1:] if gt > arr[0]])

import sys
sys.setrecursionlimit(99999)


def quick_sort_normal(arr, start, end):
    if start >= end:
        return
    temp = arr[start]
    index = start
    s = start
    e = end
    s += 1
    while s <= e:
        if temp > arr[e]:
            arr[index] = arr[e]
            index = e
        else:
            e -= 1
            continue
        if temp < arr[s]:
            arr[index] = arr[s]
            index = s
        else:
            s += 1
    arr[index] = temp
    #print arr
    quick_sort_normal(arr, start, index-1)
    quick_sort_normal(arr, index+1, end)


if __name__ == "__main__":
    import random

    b = [random.randint(1, 100) for i in xrange(20)]
    print b
    b = quick_sort(b)
    print 'after sort: ', b

    random.shuffle(b)
    print 'before sort ', b
    quick_sort_normal(b, 0, len(b)-1)
    print 'after sort ', b