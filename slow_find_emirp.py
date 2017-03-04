def is_prime(n):
    if n>10 :
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    return False
def find_emirp(n):
    a=[]
    flag3=True
    for i in range(n):
        flag1=is_prime(i)
        flag2=is_prime(int(str(i)[::-1]))
        if flag1 and flag2 and i != int(str(i)[::-1]):
            a.append(i)
    try:
        return [len(a),max(a),sum(a)]
    except:
        return [len(a),0,sum(a)]
