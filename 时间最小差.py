class Solution(object):
    def findMinDifference(self, timePoints):
        res = []
        timePoints=sorted(timePoints)
        for i in range(len(timePoints)-1):
            a1 = timePoints[i]
            a2 = timePoints[i+1]
            num1=int(a1[:2])*60+int(a1[3:])
            num2=int(a2[:2])*60+int(a2[3:])
            if abs(num1-num2)>=12*60:
                res.append(abs(abs(num1-num2)-24*60))
            else:
                res.append(abs(num1-num2))
        a1 = timePoints[0]
        a2 = timePoints[len(timePoints)-1]
        num1=int(a1[:2])*60+int(a1[3:])
        num2=int(a2[:2])*60+int(a2[3:])
        if abs(num1-num2)>=12*60:
            res.append(abs(abs(num1-num2)-24*60))
        else:
            res.append(abs(num1-num2))
        return min(res)
print Solution().findMinDifference(["05:31","22:08","00:35"])