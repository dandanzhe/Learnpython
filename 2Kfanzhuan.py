class Solution(object):
    def reverseStr(self, s, k):
        a=[]
        num = len(s)/(2*k)
        for i in range(num):
            a.append(s[i*k:i*k+k][::-1])
            a.append(s[i*k+k:i*k+2*k])
        if len(s[num*k:])<k:
            return "".join(a)+s[num*k:]
        else:
            return "".join(a)+s[num*2*k:num*2*k+k][::-1]+s[num*2*k+k:]

print Solution().reverseStr("abcdefg",2)