def log(f):
    @functools.wraps(f)
    def wrapper(x):
        print 'call...'
        return f(x)
    return wrapper