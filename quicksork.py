# -*- coding:utf-8 -*-

def quicksort1(arr):
	if len(arr) < 2:
		return arr
	return quicksort1([le for le in arr[1:] if le <= arr[0]]) + arr[0:1] + quicksort1([gt for gt in arr[1:] if gt > arr[0]])



if __name__ == "__main__":
	import random
	b = [random.randint(1,100) for i in xrange(20) ]
	print b
	b = quicksort1(b)
	print 'after sort: ', b