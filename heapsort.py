# -*- coding=utf-8 -*-

"""
堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法.
用一个列表来存储堆（和用数组存储类似），对于处在i位置的元素，2*i+1位置上的是其左孩子，2*i+2是其右孩子，类似得可以得出该元素的父元素。
首先我们写一个函数，对于某个子树，从根节点开始，如果其值小于子节点的值，就交换其值。用此方法来递归其子树。
接着，我们对于堆的所有非叶节点，自下而上调用先前所述的函数，得到一个树，对于每个节点（非叶节点），它都大于其子节点。
在完成之后，将列表的头元素和尾元素调换顺序，这样列表的最后一位就是最大的数，接着在对列表的0到n-1部分再调用以上建立最大堆的过程。
"""


def left_child(node):
    return 2 * node + 1


def right_child(node):
    return 2 * node + 2


def parent(i):
    return i % 2 and (i - 1) / 2 or (i - 2) / 2


def max_heapify(arr, i, heap_size):
    left = left_child(i)
    right = right_child(i)

    largest = i  # 父节点，子节点中最大的元素

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, heap_size)


def built_max_heap(arr):
    length = len(arr)
    for i in range(length//2, -1, -1):  # 对非叶节点调用上述函数，构建大顶堆
        max_heapify(arr, i, length)


def heap_sort(arr):
    built_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i)


if __name__ == "__main__":
    import random

    b = [random.randint(1, 1000) for i in xrange(200)]
    print 'before sort: ', b
    heap_sort(b)
    print 'after sorted: ', b