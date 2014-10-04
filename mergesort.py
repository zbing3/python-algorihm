#-*- coding=utf-8 -*-

""" 对于一个子序列，分成两份，比较两份的第一个元素，小者弹出，然后重复这个过程。
    对于待排序列，以中间值分成左右两个序列，然后对于各子序列再递归调用。
    总而言之，就是先分后和。
"""


def merge(arr, start, end, mid):
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    for i in xrange(start, end+1):
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr[i] = left.pop(0)
            else:
                arr[i] = right.pop(0)
        elif len(right) == 0 and len(left) != 0:
            arr[i] = left.pop(0)
        elif len(left) == 0 and len(right) != 0:
            arr[i] = right.pop(0)


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, end, mid)

if __name__ == "__main__":
    import random

    b = [random.randint(1, 100) for i in xrange(20)]
    print 'before sort: ', b
    merge_sort(b, 0, len(b))
    print 'after sorted: ', b