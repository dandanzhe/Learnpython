#!/usr/bin/env python
#coding=utf-8

def sum_pairs(ints, s):
    for i in range(1,len(ints)):
        for j in range(len(ints)-i):
            if ints[j]+ints[j+i]==s:
                print [ints[j],ints[j+i]]
                return [ints[j],ints[j+i]]
            continue
    print "None"
    return None

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]
sum_pairs(l8, 10)
sum_pairs(l7, 0)

#数据大更好
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
