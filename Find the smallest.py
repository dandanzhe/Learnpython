import itertools
def smallest(n):
    a=[]
    result=[]
    for i in str(n):
        a.append(i)
    res=list(itertools.permutations(a,len(a)))
    for i in res:
        result.append("".join(i))
    print min(result)
smallest(261235)