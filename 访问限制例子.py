class Person(object):
    def __init__(self, score):
        self.__score = score
    def get_score(self):
        return self.__score

p = Person(100)
setattr(p, '__score', 88)
print p.get_score
print p.__score
print p._Person__score