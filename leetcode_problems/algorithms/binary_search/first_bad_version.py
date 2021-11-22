def isBadVersion(version: int):
    if(version >= 1):
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        leftValue, rightValue = 1, n
        while leftValue < rightValue:
            pivot = leftValue + (rightValue - leftValue) // 2
            if isBadVersion(pivot):
                rightValue = pivot
            else:
                leftValue = pivot + 1
        return leftValue


print(Solution().firstBadVersion(1))
