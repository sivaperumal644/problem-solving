from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIndex, rightIndex = 0, len(nums) - 1
        while leftIndex <= rightIndex:
            pivot = leftIndex + (rightIndex - leftIndex) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                rightIndex = pivot - 1
            else:
                leftIndex = pivot + 1
        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
