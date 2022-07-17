"""Implementations of some sorting"""
import random
import ArrayList

def linear_search(a : ArrayList.ArrayList(), x):
    # todo
    for i in range(0, a.size() - 1):
        if x == a[i]:
            return i
    return -100

def binary_search(a : ArrayList.ArrayList(), x):
    # todo
    l = 0
    r = a.size() - 1
    while r > l:
        m = ((l + r) // 2)
        if x == a[m]:
            return m
        elif x < a[m]:
            r = m + 1
        else:
            l = m + 1
    return -100

def _merge(a0 : ArrayList.ArrayList(), a1 : ArrayList.ArrayList(), a : ArrayList.ArrayList()):
    # todo
    l = 0
    r = 0
    for i in range(0, a.size()):
        if l >= a0.size():
            a.set(i, a1.get(r))
            r += 1
        elif r >= a1.size():
            a.set(i, a0.get(l))
            l += 1
        elif a0.get(l) <= a1.get(r):
            a.set(i, a0.get(l))
            l += 1
        else:
            a.set(i, a1.get(r))
            r += 1
    return

def merge_sort(a : ArrayList.ArrayList()):
    # todo
    if a.size() <= 1:
        return a
    a0 = ArrayList.ArrayList()
    a1 = ArrayList.ArrayList()
    m = a.size() // 2

    for i in range(0, m):
        a0.append(a.get(i))
    for i in range(m, a.size()):
        a1.append(a.get(i))

    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)
    return

def _partition_f(a : ArrayList, start, end):
    l = start + 1
    r = end
    pivot = a.get(start)
    crossed = False
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l += 1
        while r >= l and a.get(r) >= pivot:
            r -= 1
        if l < r:
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else:
            crossed = True
    a.set(start, a.get(r))
    a.set(r, pivot)
    return r

def _partition_r(a : ArrayList, start, end):
    index = random.randint(start, end)
    random_element = a.get(index)
    a.set(index, a.get(start))
    a.set(start, random_element)
    pivot = a.get(start)
    crossed = False
    l = start + 1
    r = end
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l += 1
        while r >= l and a.get(r) >= pivot:
            r -= 1
        if l < r:
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else:
            crossed = True
    a.set(start, a.get(r))
    a.set(r, pivot)
    return r

def _quick_sort_f(a : ArrayList.ArrayList, start, end):
    # todo
    if start < end:
        p = _partition_f(a, start, end)
        _quick_sort_f(a, start, p-1)
        _quick_sort_f(a, p+1, end)

def _quick_sort_r(a : ArrayList.ArrayList, start, end):
    # todo
    if start < end:
        p = _partition_r(a, start, end)
        _quick_sort_r(a, start, p-1)
        _quick_sort_r(a, p + 1, end)

def quick_sort(a : ArrayList.ArrayList(), p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size()-1)
    else:
        _quick_sort_f(a, 0, a.size()-1)


    
