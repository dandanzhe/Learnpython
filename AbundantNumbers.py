#https://www.codewars.com/kata/57f3996fa05a235d49000574/train/python
def abundant(h):
    for i in range(h+1)[::-1]:
        sum = 0
        for j in xrange(1,i):
            if i%j==0:
                sum += j
        if sum>h:
            return [[i],[sum-i]]
print abundant(1000523)