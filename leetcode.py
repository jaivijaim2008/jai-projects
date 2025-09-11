
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        for i in l1[::-1]:
            lii1=i
        for i in l2[::-1]:
            lii2=i
        for i in lii1:
            for j in  lii2:
                
                n=i+j
a=[2,4,3]
b=[5,6,4]
c=Solution().addTwoNumbers(a,b)