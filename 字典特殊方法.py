#-*- coding:utf8 -*-
#python中__getitem__, __setitem__, __delitem__的使用
#用于索引操作，如字典。以上分别表示获取、设置、删除数据

class C(object):
    def __init__(self):
        self.value = {}
        self.name = 'Xuzhe'

    def __getitem__(self, item):
        print '__getitem__', item
        return self.value[item]

    def __setitem__(self, key, value):
        print '__setitem__', key, value
        self.value[key] = value

    def __delitem__(self, key):
        print '__delitem__', key
        del self.value[key]
    def __len__(self):
        return len(self.value)

print C.__doc__

c = C()
#print c
#result = c['k1']
c['k2'] = 5
c['k1'] = "Hello"
print c['k2']
print len(c)