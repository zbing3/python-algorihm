# -*- coding: utf-8 -*-  

"""插入排序:
        1、假设一个数组A=[2,8,5,4,9,13,23]。
        2、另外假设一个数组B，B用来保存A中排好序的元素。
        3、将A中的第一个元素插入到B中，B=[2]
        4、选择A中下一个元素，与B中的元素比较，找到合适的插入位置, 然后往后移插入位置之后的元素。
        5、重复步骤4，直到A中的元素全部遍历。
"""


def insert_sort(A):
    length = len(A)
    if length == 0:
        return
    B = A[0:1]  # 将A中的第一个元素加到B中
    for tag in range(1, length):
        if A[tag] > B[tag-1]:
            B.append(A[tag])
            continue
        temp = A[tag]
        for i in range(tag):
            if temp < B[i]:
                B[i], temp = temp, B[i]
        B.append(temp)

    return B


#不新建数组保存已排好序的元素，直接使用原数组
def insert_sort_(A):
    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            for j in range(i - 1, 0, -1):
                if A[j] < A[j - 1]:
                    A[j], A[j - 1] = A[j - 1], A[j]
                else:
                    break


#折半插入排序，减少空间复杂度
def binary_insert_sort(a):
    for i in range(1, len(a)):
        low = 0
        high = i - 1
        while low <= high:
            m = (low + high) // 2
            if a[m] <= a[i]:
                low = m + 1
            else:
                high = m - 1
        for j in range(i - 1, high, -1):
            a[j + 1], a[j] = a[j], a[j + 1]


# 2-路插入排序，在折半插入排序的基础上再改进，减少移动次数
def two_insert_sort(a):
    #
    length = len(a)
    c = a[:]
    first = length  #
    final = 0
    for i in range(1, len(a)):
        if a[i] < c[0]:
            c[first - 1] = a[i]
            low = first
            high = length - 1  #
            while low <= high:
                m = (low + high) // 2
                if a[i] < c[m]:
                    high = m - 1
                else:
                    low = m + 1
            for j in range(first, high + 1):
                c[j - 1], c[j] = c[j], c[j - 1]  #
            first -= 1

        else:
            c[final + 1] = a[i]
            low = 1
            high = final
            while low <= high:
                m = (low + high) // 2
                if a[i] < c[m]:
                    high = m - 1
                else:
                    low = m + 1
            for j in range(final, high, -1):
                c[j + 1], c[j] = c[j], c[j + 1]  #
            final += 1
    return c


def shell_insert(a, dk):
    length = len(a)
    for x in xrange(dk + 1, length):
        if a[x] < a[x - dk]:
            for y in xrange(x, dk - 1, -dk):
                if a[y] < a[y - dk]:
                    a[y], a[y - dk] = a[y - dk], a[y]
                else:
                    break


def shell_sort(a):
    dk = len(a)
    while dk >= 1:
        dk = dk // 2
        shell_insert(a, dk)


if __name__ == '__main__':
    import random

    b = [random.randint(1, 100) for i in xrange(20)]
    print 'before insert_sort ', b
    insert_sort(b)
    print 'insert_sort 1 ', insert_sort(b)

    print 'before insert sort ', b
    insert_sort_(b)
    print 'after insert sort ', b

    random.shuffle(b)
    print 'before binary insert sort ', b
    binary_insert_sort(b)
    print 'after binary insert sort ', b

    random.shuffle(b)
    print 'before two routine insert sort ', b
    print 'after two routine insert sort  ', two_insert_sort(b)

    random.shuffle(b)
    print 'before shell sort ', b
    shell_sort(b)
    print 'after shellSort ', b