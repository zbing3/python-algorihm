import random

def insertSort(a):
	l = len(a)
	i = 1
	while i < l:
		if a[i] < a[i-1]:
			temp = a[i]
			a[i] = a[i-1]
			j = i-1
			while j > 0:
				if temp < a[j-1]:
					a[j] = a[j-1]
					j -= 1
				else:
					break
			a[j] = temp
		i += 1


def insertSort2(a):
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			a[i], a[i-1] = a[i-1], a[i]
			for j in range(i-1, 0, -1):
				if a[j] < a[j-1]:
					a[j], a[j-1] = a[j-1], a[j]
				else:
					break


def bInsertSort(a):
	for i in range(1, len(a)):
		low = 0
		high = i - 1
		while(low <= high):
			m = (low + high) // 2
			if a[m] <= a[i]:
				low = m + 1
			else:
				high = m - 1
		for j in range(i-1, high, -1):
			a[j+1], a[j] = a[j], a[j+1]



def tInsertSort(a):
	#set another array c for store the sorted list
	length = len(a) 
	c = a[:]
	first = length
	final = 0
	for i in range(1, len(a)):
		if a[i] < c[0]:
			c[first-1] = a[i]
			low = first
			high = length-1
			while low <= high:
				m = (low + high) // 2
				if a[i] < c[m]:
					high = m - 1
				else:
					low = m + 1
			for j in range(first, high+1):
				c[j-1], c[j] = c[j], c[j-1] #the small element move to right
			first -= 1

		else:
			c[final+1] = a[i]
			low = 1
			high = final
			while low <= high:
				m = (low + high) // 2
				if a[i] < c[m]:
					high = m - 1
				else:
					low = m + 1
			for j in range(final, high, -1):
				c[j+1], c[j] = c[j], c[j+1] #the bigger element move to left
			final += 1
	return c


if __name__ == '__main__':
	b = [random.randint(1,1000) for i in xrange(200) ]
	print b
	insertSort(b)
	print 'insertSort 1 ',b
	random.shuffle(b)
	print 'shuffle b ', b
	insertSort2(b)
	print 'insertSort 2 ', b
	random.shuffle(b)
	print 'shuffle b ', b
	bInsertSort(b)
	print 'bInsertSort ', b

	random.shuffle(b)
	print 'shuffle b ', b
	
	print 'tInsertSort ', tInsertSort(b)
	