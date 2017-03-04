def unpack(l):
    res = []
    for x in l:
        if x == None: res.append(x)
        elif type(x) in [str,int,None]: res.append(x)
        elif type(x) == list: res += unpack(x)
        elif type(x) in [set,tuple]: res += unpack(list(x))
        elif type(x) == dict: res += unpack(x.keys()) + unpack(x.values())
    return res
unpack([None, [1, ({2, 3}, {'foo': 'bar'})]])
