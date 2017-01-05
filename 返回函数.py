def calc_prod(lst):
    def ji():
        def f(x,y):
			return x*y
        return reduce(f,lst,1)
    return ji
f = calc_prod([1, 2, 3, 4])
print f()