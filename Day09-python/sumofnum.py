class Solution:
    def findSum(self, n):
        s = 0
        for i in range(1, n + 1):
            s = s + i
        return s
obj = Solution()
print(obj.findSum(5))
