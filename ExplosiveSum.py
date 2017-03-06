#!/usr/bin/env python
#coding=utf-8
#How many ways can you make the sum of a number?
def exp_sum(n):
    if n < 0:
      return 0
    dp = [1]+[0]*n
#    print dp
    for num in xrange(1,n+1):
      for i in xrange(num,n+1):
        dp[i] += dp[i-num]
#        print 'dp[%s]=%s'%(i,dp[i])
#        print 'dp[%s]=%s'%(i-num,dp[i-num])
    return dp[-1]
exp_sum(8)