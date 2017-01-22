class User(object):
    def __init__(self):
        self.rank=-8
        self.progress=0
    def inc_progress(self,num):
        if num>0 and self.rank<0:
            self.progress += (num-self.rank-1)**2*10
            if self.progress>=100 and self.rank<8:
                self.rank += self.progress//100
                self.progress = self.progress%100
                if self.rank>=0:
                    self.rank += 1
                elif self.rank>=8:
                    self.rank=8
                    self.progress=0
        elif num<0 and num>self.rank:
            self.progress += (num-self.rank)**2*10
            if self.progress>=100 and self.rank<8:
                self.rank += self.progress//100
                self.progress = self.progress%100
                if self.rank>=0:
                    self.rank += 1
                elif self.rank>=8:
                    self.rank=8
                    self.progress=0
        elif num==self.rank:
            self.progress += 3
            if self.progress>=100 and self.rank<8:
                self.rank += self.progress//100
                self.progress = self.progress%100
                if self.rank==0:
                    self.rank += 1
             if self.rank==8:
                 self.progress=0
        elif num<self.rank:
            self.progress += 1
            if self.progress>=100 and self.rank<8:
                self.rank += self.progress//100
                self.progress = self.progress%100
                if self.rank==0:
                    self.rank += 1
                elif self.rank>=8:
                    self.rank=8
                    self.progress=0
        elif num>0 and num>self.rank and self.rank>0:
            self.progress += (num-self.rank)**2*10
            if self.progress>=100 and self.rank<8:
                self.rank += self.progress//100
                self.progress = self.progress%100
                if self.rank>=8:
                    self.rank=8
                    self.progress=0
l=[-4,-4,-2,2,2,2,2,3,1,2,-1,4,4,5,6,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
a=User()
for i in l:
    print 'rank=%d'%a.rank
    print 'progress=%d'%a.progress
    a.inc_progress(i)
    print "num=%d"%i
    print 'rank=%d'%a.rank
    print 'progress=%d'%a.progress
