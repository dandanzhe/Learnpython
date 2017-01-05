# -*-coding:UTF-8 -*-
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)#最大公约数

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / self.q


print float(Rational(7, 2))
print float(Rational(1, 3))