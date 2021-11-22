from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # ********** Brute Force Method ******************
        # for i in range(0, len(nums)):
        #     if nums[i] >= target:
        #         return i
        #     if i == len(nums) - 1:
        #         return i + 1

        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low


print(Solution().searchInsert([1], 0))
