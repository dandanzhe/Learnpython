def derivative(n):
    a=n.split("+")
    # print a
    for i in range(len(a)):
        if 'x' not in a[i]:
            a[i]=""
        elif a[i][-1]=="x":
            a[i]=a[i][:-1]
        else:
            b=a[i].split("x^")
            if b[0]=="" and b[1]=='2':
                a[i]="%sx"%(b[0])
            elif b[0]=="":
                a[i]="%sx^%s"%(b[0],int(b[0])-1)
            else:
                # if b[0]=="":
                #     b[0]=1
                a[i]="{0}x^{1}".format(int(b[0])*int(b[1]),int(b[1])-1)
    print a
    print "+".join(a)[:-1]
    return "".join(a)[:-1]
derivative("2x^2+2x+1")


#other's solution
# import re
# str2int = lambda s: int(s + '1' * (not s[-1:].isdigit()))

# def monomial(args):
#     c, p = map(str2int, args)
#     return '%+d' % (c * p) + 'x' * (p > 1) + '^%d' % (p - 1) * (p > 2)

# def derivative(eq):
#     return ''.join(map(monomial, re.findall("(-?\d*)x\^?(\d*)", eq))).lstrip('+') or '0'