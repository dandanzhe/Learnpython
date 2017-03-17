#http://www.codewars.com/kata/twice-linear/train/python
def dbl_linear(n):
    a = [1]
    i = 0
    while i < n*2:
        a.append(a[i]*2+1)
        a.append(a[i]*3+1)
        i += 1
    b=sorted(set(a))
    print b
    return list(b)[n]
print dbl_linear(50)