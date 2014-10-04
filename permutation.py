def permutation_static(max):
    index = [0] * max

    while True:
        candi = range(0, max)
        for i in range(1, max + 1):
            print candi.pop(index[-i])
        index[1] += 1
        i = 1
        while i < max - 1 and index[i] > i:
            index[i] = 0
            index[i + 1] += 1
            i += 1
        if index[-1] >= max:
            break


def addperm(x, l):
    print l
    return [l[0:i] + [x] + l[i:] for i in range(len(l) + 1)]


def perm(l):
    print l
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0], y)]


def perm(a, k=0):
    if k == len(a):
        print a
    else:
        for i in xrange(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k + 1)
            a[k], a[i] = a[i], a[k]


def permutList(l):
    if not l:
        return [[]]
    res = []
    for e in l:
        temp = l[:]
        temp.remove(e)
        res.extend([[e] + r for r in permutList(temp)])

    return res


def permutations(head, tail):
    if len(head) == 0:
        print tail
    else:
        for i in range(len(head)):
            tail.append(head[i])
            permutations(head[0:i] + head[i + 1:], tail)
            tail.remove(head[i])


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]