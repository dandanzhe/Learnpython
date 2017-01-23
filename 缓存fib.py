ca={}
def fib_cache(num):
    if num <=2:
        return num
    elif num > 2:
        if num in ca:
            return ca[num]
        ca[num]=fib_cache(num-1)+fib_cache(num-2)
        return ca[num]
    else:
        print "wrong number"
